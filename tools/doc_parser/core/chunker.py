from typing import List
import difflib
from .models import Slide, Chunk

class SlideChunker:
    """
    Відповідає за семантичне групування слайдів.
    Вирішує проблему "розірваного контексту", коли одна тема (напр., "Спіральна модель") 
    розтягнута на кілька слайдів.
    """
    
    @staticmethod
    def chunk_slides(slides: List[Slide], max_pages_per_chunk: int = 5) -> List[Chunk]:
        """
        Групує послідовні слайди з однаковим (або дуже схожим) заголовком в один Chunk.
        Якщо розмір чанку перевищує max_pages_per_chunk (що критично для книг), 
        примусово створюється новий чанк.
        """
        if not slides:
            return []
            
        chunks = []
        current_chunk = Chunk(title=slides[0].title, pages=[slides[0]])
        
        for slide in slides[1:]:
            is_same = False
            
            # Якщо ми вже досягли ліміту сторінок для одного чанку, примусово розриваємо
            if len(current_chunk.pages) >= max_pages_per_chunk:
                is_same = False
            else:
                if slide.title and current_chunk.title:
                    t1 = slide.title.strip().lower()
                    t2 = current_chunk.title.strip().lower()
                    # Використовуємо fuzzy matching (подібність > 80%), щоб опечатки OCR не розривали чанк
                    if t1 == t2 or difflib.SequenceMatcher(None, t1, t2).ratio() > 0.8:
                        is_same = True
                elif not slide.title or slide.title.strip() == "":
                    # Якщо на поточному слайді немає заголовка взагалі, це гарантовано продовження попереднього слайда!
                    is_same = True
            
            # Якщо заголовок такий самий (або дуже схожий, або відсутній) — це продовження теми
            if is_same:
                slide.is_continuation = True
                current_chunk.pages.append(slide)
            else:
                # Тема змінилася або перевищено ліміт, закриваємо поточний чанк і створюємо новий
                chunks.append(current_chunk)
                current_chunk = Chunk(title=slide.title, pages=[slide])
                
        # Додаємо останній чанк
        chunks.append(current_chunk)
        return chunks
