import os
import hashlib
import fitz
from typing import List, Set
from core.models import ImageMeta, Slide

class PDFExtractor:
    """
    Екстрактор для класичних PDF-книг та посібників.
    
    Особливості:
    - Використовує get_text("dict") для витягування ЛИШЕ тих зображень, які реально відрендерені на сторінці (type == 1), ігноруючи вшиті фони/тіні.
    - Фільтрує дрібні графічні елементи (менше 25000 пікселів за площею).
    - Має базову евристику для пошуку заголовків розділів, що дозволяє чанкеру склеювати сторінки однієї глави.
    """
    
    def __init__(self, pdf_path: str, images_dir: str):
        self.pdf_path = pdf_path
        self.images_dir = images_dir
        self.doc = fitz.open(pdf_path)
        os.makedirs(self.images_dir, exist_ok=True)

    def _extract_title(self, page: fitz.Page) -> str:
        """
        Знаходить найбільший текст у верхній третині сторінки.
        Якщо текст значно більший за середній шрифт сторінки, він вважається заголовком.
        """
        blocks = page.get_text("dict").get("blocks", [])
        text_blocks = [b for b in blocks if b["type"] == 0]
        if not text_blocks:
            return ""
            
        page_height = page.rect.height
        candidates = []
        
        # Знаходимо всі текстові спани у верхній третині
        for block in text_blocks:
            y0 = block.get("bbox", [0, 0, 0, 0])[1]
            if y0 > page_height * 0.33:
                continue # Ігноруємо все, що нижче верхньої третини
                
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span.get("text", "").strip()
                    if text and len(text) > 3:
                        candidates.append({
                            "text": text,
                            "size": span.get("size", 0),
                            "y0": y0,
                            "bold": "bold" in span.get("font", "").lower()
                        })
                        
        if not candidates:
            return ""
            
        # Знаходимо максимальний шрифт на сторінці
        max_size = max(c["size"] for c in candidates)
        
        # Беремо всі тексти з "великим" шрифтом (допускаємо відхилення -2pt)
        top_candidates = [c for c in candidates if c["size"] >= max_size - 2]
        if not top_candidates:
            return ""
            
        # Обираємо той, що найвище (найменший y0)
        top_candidates.sort(key=lambda x: x["y0"])
        best_text = top_candidates[0]["text"]
        
        # Якщо шрифт менший за 14pt (стандартний текст книги), це навряд чи заголовок
        if top_candidates[0]["size"] < 14 and not top_candidates[0]["bold"]:
            return ""
            
        return best_text

    def extract_slides(self) -> List[Slide]:
        """
        Проходить по сторінках PDF, витягує сирий текст та справжні зображення.
        """
        slides = []
        
        for page_num in range(len(self.doc)):
            page = self.doc[page_num]
            raw_text = page.get_text("text", sort=True).strip()
            title = self._extract_title(page)
            
            # Рендеримо сторінку для LLM
            full_img_name = f"page_{page_num+1}_full.jpeg"
            full_img_path = os.path.join(self.images_dir, full_img_name)
            if not os.path.exists(full_img_path):
                pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5))
                pix.save(full_img_path)
            
            # Витягуємо зображення за допомогою блокового словника
            images = []
            blocks = page.get_text("dict").get("blocks", [])
            img_index = 0
            
            for block in blocks:
                # type == 1 означає блок зображення
                if block["type"] == 1:
                    width = block.get("width", 0)
                    height = block.get("height", 0)
                    area = width * height
                    
                    # Жорсткий фільтр для мікроелементів (декоративні лінії, буліти)
                    # 25000 пікселів - це приблизно квадрат 150x150
                    if width < 100 or height < 100 or area < 25000:
                        continue
                        
                    image_bytes = block.get("image")
                    if not image_bytes:
                        continue
                        
                    img_hash = hashlib.md5(image_bytes).hexdigest()
                    ext = block.get("ext", "jpeg")
                    img_index += 1
                    
                    image_name = f"page_{page_num+1}_img_{img_index}.{ext}"
                    image_path = os.path.join(self.images_dir, image_name)
                    
                    if not os.path.exists(image_path):
                        with open(image_path, "wb") as f:
                            f.write(image_bytes)
                            
                    images.append(ImageMeta(
                        path=image_path,
                        width=width,
                        height=height,
                        hash=img_hash
                    ))
                    
            slides.append(Slide(
                page_num=page_num,
                raw_text=raw_text,
                images=images,
                title=title,
                full_image_path=full_img_path
            ))
            
        return slides
