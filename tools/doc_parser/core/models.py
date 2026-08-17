from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class ImageMeta:
    """Метадані зображення, знайденого на сторінці/слайді."""
    path: str
    width: int
    height: int
    hash: str
    bbox: Optional[tuple] = None  # Координати для PPTX-фільтрації (x0, y0, x1, y1)

@dataclass
class Page:
    """Базова структура для сторінки (книги)."""
    page_num: int
    raw_text: str
    images: List[ImageMeta] = field(default_factory=list)
    full_image_path: Optional[str] = None

@dataclass
class Slide(Page):
    """Специфічна структура для слайду презентації."""
    title: str = ""
    # Для PPTX важливо відстежувати, чи є цей слайд продовженням попереднього
    is_continuation: bool = False 

@dataclass
class Chunk:
    """
    Семантичний блок, який відправляється в LLM.
    Для книг — це 2-3 об'єднані сторінки (Page).
    Для PPTX — це набір слайдів (Slide) з однаковим заголовком.
    """
    title: str
    pages: List[Page] = field(default_factory=list)
    
    @property
    def all_images(self) -> List[ImageMeta]:
        """Повертає список унікальних картинок з усіх сторінок чанку."""
        unique_images = []
        seen_hashes = set()
        for page in self.pages:
            for img in page.images:
                if img.hash not in seen_hashes:
                    unique_images.append(img)
                    seen_hashes.add(img.hash)
        return unique_images
    
    @property
    def combined_text(self) -> str:
        """Склеює сирий текст усіх сторінок для відправки в LLM."""
        return "\n\n---\n\n".join([p.raw_text for p in self.pages])
