import os
import sys
from google import genai

def main():
    keys = sys.argv[1:]
    if not keys:
        env_keys = os.environ.get("GEMINI_API_KEYS")
        if env_keys:
            keys = [k.strip() for k in env_keys.split(",") if k.strip()]
            
    if not keys:
        print("❌ Передайте ключі через аргументи або GEMINI_API_KEYS")
        return
        
    print(f"🔍 Перевірка {len(keys)} ключів...\n")
    for idx, key in enumerate(keys):
        masked = key[:6] + "..." + key[-4:] if len(key) > 10 else key
        try:
            client = genai.Client(api_key=key)
            # Робимо легкий запит
            client.models.generate_content(model="gemini-3.5-flash-lite", contents="ping")
            print(f"✅ Ключ {idx+1} ({masked}): ПРАЦЮЄ")
        except Exception as e:
            err = str(e)
            if "401" in err or "UNAUTHENTICATED" in err:
                print(f"❌ Ключ {idx+1} ({masked}): БИТИЙ (401 UNAUTHENTICATED) <- ОСЬ ВІН!")
            elif "429" in err or "quota" in err.lower():
                print(f"⚠️ Ключ {idx+1} ({masked}): ВИЧЕРПАНО ЛІМІТ (429)")
            elif "0" in err and "quota_limit_value" in err:
                print(f"💀 Ключ {idx+1} ({masked}): РЕГІОНАЛЬНИЙ БАН (Квота 0)")
            else:
                print(f"❓ Ключ {idx+1} ({masked}): ПОМИЛКА ({err})")

if __name__ == "__main__":
    main()
