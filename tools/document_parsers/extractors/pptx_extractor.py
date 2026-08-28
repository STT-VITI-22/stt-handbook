import os
import hashlib
import fitz
from typing import List, Set
from core.models import ImageMeta, Slide

class PPTXExtractor:
    """
    Екстрактор для PDF-файлів, згенерованих з презентацій (PPTX).
    
    Відповідальності:
    - Витягування сирого тексту та зображень з кожної сторінки.
    - Динамічна фільтрація водяних знаків та логотипів (зображень, що повторюються на >20% слайдів).
    - Евристичне визначення заголовка слайду (за найбільшим розміром шрифту) для подальшого групування.
    """
    
    def __init__(self, pdf_path: str, images_dir: str):
        self.pdf_path = pdf_path
        self.images_dir = images_dir
        self.doc = fitz.open(pdf_path)
        os.makedirs(self.images_dir, exist_ok=True)
        
    def _get_global_watermarks(self) -> Set[str]:
        """
        Знаходить хеші зображень, які зустрічаються занадто часто (логотипи, фони).
        Поріг: більше 5 разів або присутні на >20% слайдів.
        """
        hash_counts = {}
        for page in self.doc:
            for img in page.get_images(full=True):
                xref = img[0]
                base_image = self.doc.extract_image(xref)
                if "image" in base_image:
                    img_hash = hashlib.md5(base_image["image"]).hexdigest()
                    hash_counts[img_hash] = hash_counts.get(img_hash, 0) + 1
                    
        threshold = max(5, int(len(self.doc) * 0.2))
        return {h for h, count in hash_counts.items() if count > threshold}

    def _extract_title(self, page: fitz.Page) -> str:
        """
        Визначає заголовок слайду, шукаючи текстовий блок із найбільшим розміром шрифту у верхній частині сторінки.
        Якщо є кілька великих блоків, обирає найвищий з них.
        """
        blocks = page.get_text("dict").get("blocks", [])
        text_blocks = [b for b in blocks if b.get("type") == 0]
        if not text_blocks:
            return ""
            
        candidates = []
        page_height = page.rect.height
        global_max = 0
        
        for block in text_blocks:
            bbox = block.get("bbox", [0, 0, 0, 0])
            y0 = bbox[1]
            
            # Заголовок слайду майже завжди знаходиться у верхніх 15% сторінки
            if y0 > page_height * 0.15: 
                continue
                
            max_size = 0
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    if not span.get("text", "").strip(): 
                        continue
                    if span.get("size", 0) > max_size: 
                        max_size = span["size"]
                        
            if max_size > 0:
                candidates.append({"y0": y0, "size": max_size, "block": block})
                if max_size > global_max: 
                    global_max = max_size
                    
        if not candidates or global_max < 12: 
            return ""
            
        # Фільтруємо кандидатів: залишаємо лише тих, чий розмір шрифту близький до максимального
        top_candidates = [c for c in candidates if c["size"] >= global_max - 4]
        
        # Серед них обираємо той, що найвище (найменший y0)
        top_candidates.sort(key=lambda x: x["y0"])
        best_block = top_candidates[0]["block"]
        
        title_lines = []
        for line in best_block.get("lines", []):
            line_text = "".join([span.get("text", "") for span in line.get("spans", [])])
            if line_text.strip(): 
                title_lines.append(line_text.strip())
                
        return " ".join(title_lines).strip()

    def extract_slides(self) -> List[Slide]:
        """
        Основний метод. Проходить по всіх сторінках, зберігає картинки, 
        відкидає сміття та повертає масив об'єктів Slide.
        """
        watermarks = self._get_global_watermarks()
        slides = []
        
        for page_num in range(len(self.doc)):
            page = self.doc[page_num]
            raw_text = page.get_text("text", sort=True).strip()
            title = self._extract_title(page)
            
            # Рендеримо весь слайд для того, щоб LLM бачила загальний контекст (де і як розташовані картинки)
            full_img_name = f"page_{page_num+1}_full.jpeg"
            full_img_path = os.path.join(self.images_dir, full_img_name)
            if not os.path.exists(full_img_path):
                pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5))  # Середня якість для контексту
                pix.save(full_img_path)
            
            images = []
            for img_index, img in enumerate(page.get_images(full=True)):
                xref = img[0]
                base_image = self.doc.extract_image(xref)
                if "image" not in base_image:
                    continue
                    
                image_bytes = base_image["image"]
                img_hash = hashlib.md5(image_bytes).hexdigest()
                
                # Відкидаємо водяні знаки та логотипи
                if img_hash in watermarks:
                    continue
                    
                width = base_image.get("width", 0)
                height = base_image.get("height", 0)
                
                # Відкидаємо занадто малі елементи (іконки, буліти)
                if width < 100 or height < 100:
                    continue
                    
                ext = base_image["ext"]
                image_name = f"page_{page_num+1}_img_{img_index+1}.{ext}"
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
