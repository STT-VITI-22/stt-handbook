import os
import json
import time
import random
import threading
from datetime import date
from typing import List
from google import genai
from tqdm import tqdm

from google.genai import types

class KeyPool:
    """Керує пулом API ключів, відстежує їх використання та блокування."""
    def __init__(self, keys: List[str], db_path: str = "api_usage.json"):
        self.keys = list(set(k.strip() for k in keys if k.strip()))
        self.db_path = db_path
        self.lock = threading.Lock()
        self.dead_keys = set()
        self.today_str = date.today().isoformat()
        self.usage = self._load_db()
        
    def _load_db(self) -> dict:
        if os.path.exists(self.db_path):
            try:
                with open(self.db_path, "r") as f:
                    data = json.load(f)
                    # Reset if it's a new day
                    if data.get("_date") != self.today_str:
                        return {"_date": self.today_str}
                    return data
            except Exception:
                pass
        return {"_date": self.today_str}
        
    def _save_db(self):
        try:
            with open(self.db_path, "w") as f:
                json.dump(self.usage, f)
        except Exception as e:
            tqdm.write(f"⚠️ Помилка запису БД ключів: {e}")
            
    def record_usage(self, key: str):
        with self.lock:
            self.usage[key] = self.usage.get(key, 0) + 1
            self._save_db()
        
    def mark_dead(self, key: str):
        with self.lock:
            self.dead_keys.add(key)
        
    def get_active_keys(self) -> List[str]:
        # Денний ліміт для безкоштовних ключів Gemini - 1500
        return [k for k in self.keys if k not in self.dead_keys and self.usage.get(k, 0) < 1500]
        
    def get_best_key(self) -> str:
        active = self.get_active_keys()
        if not active:
            raise Exception("КРИТИЧНА ПОМИЛКА: Усі ключі мертві або вичерпали ліміт.")
        # Сортуємо ключі за найменшим використанням
        active.sort(key=lambda k: self.usage.get(k, 0))
        # Вибираємо випадковий з 3-х найменш навантажених (розподіл навантаження)
        return random.choice(active[:min(3, len(active))])


class GeminiClient:
    """Обгортка над Gemini API з підтримкою автоматичної ротації ключів та Rate Limiting."""
    def __init__(self, keys: List[str]):
        self.pool = KeyPool(keys)
        
    def generate(self, contents: list, model_name: str = "gemini-3.5-flash-lite") -> str:
        """Відправляє запит до API, автоматично перемикаючи ключі при помилках."""
        last_error = None
        
        # Робимо до 5 спроб з різними ключами
        for attempt in range(5):
            api_key = self.pool.get_best_key()
            client = genai.Client(api_key=api_key)
            
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=contents,
                    config=types.GenerateContentConfig(
                        safety_settings=[
                            types.SafetySetting(
                                category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                                threshold=types.HarmBlockThreshold.BLOCK_NONE,
                            ),
                            types.SafetySetting(
                                category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
                                threshold=types.HarmBlockThreshold.BLOCK_NONE,
                            ),
                            types.SafetySetting(
                                category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                                threshold=types.HarmBlockThreshold.BLOCK_NONE,
                            ),
                            types.SafetySetting(
                                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                                threshold=types.HarmBlockThreshold.BLOCK_NONE,
                            ),
                        ]
                    )
                )
                self.pool.record_usage(api_key)
                if response.text is None:
                    raise Exception("Відповідь API порожня (можливо спрацювали safety-фільтри або перевищено ліміт токенів).")
                return response.text.strip()
                
            except Exception as e:
                err_msg = str(e).lower()
                
                # Жорсткий бан або вичерпана добова квота
                if "quota" in err_msg and "exceeded" in err_msg:
                    tqdm.write(f"💀 Ключ {api_key[:6]}... вичерпав квоту. Видаляємо з пулу.")
                    self.pool.mark_dead(api_key)
                elif "403" in err_msg:
                    tqdm.write(f"💀 Ключ {api_key[:6]}... заблоковано (403). Видаляємо з пулу.")
                    self.pool.mark_dead(api_key)
                # Помилка моделі (напр., 404 NOT_FOUND)
                elif "404" in err_msg or "not found" in err_msg:
                    raise Exception(f"КРИТИЧНА ПОМИЛКА: Модель '{model_name}' не знайдена (404). Зупинка.\nПовний текст: {e}")
                # Перевантаження сервера Google (503)
                elif "503" in err_msg or "unavailable" in err_msg or "deadline" in err_msg:
                    tqdm.write(f"🐌 Сервер Google перевантажений (503). Чекаємо 10с...")
                    time.sleep(10)
                # Soft rate limit (багато запитів у хвилину 429)
                elif "429" in err_msg or "exhausted" in err_msg:
                    tqdm.write(f"⏳ Rate Limit 429 для {api_key[:6]}... Чекаємо 5с.")
                    time.sleep(5)
                else:
                    # Інша мережева помилка
                    tqdm.write(f"⚠️ Невідома помилка Gemini API: {e}")
                    time.sleep(5)
                    
        raise Exception(f"Не вдалося згенерувати контент після 5 спроб. Остання помилка: {last_error}")
