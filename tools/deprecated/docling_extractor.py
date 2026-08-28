from pathlib import Path
import os
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling_core.types.doc.document import ImageRefMode
from docling_core.types.doc.labels import PictureItem, TableItem

def parse_pdf_with_docling(pdf_path: str, output_dir: str):
    print(f"Починаємо обробку {pdf_path}...")
    
    input_doc_path = Path(pdf_path)
    out_dir = Path(output_dir)
    images_dir = out_dir / "images"
    
    out_dir.mkdir(parents=True, exist_ok=True)
    images_dir.mkdir(parents=True, exist_ok=True)

    # Налаштовуємо пайплайн, щоб він ГЕНЕРУВАВ картинки (а не викидав їх)
    pipeline_options = PdfPipelineOptions()
    pipeline_options.images_scale = 2.0
    pipeline_options.generate_page_images = False
    pipeline_options.generate_picture_images = True

    doc_converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )

    # Сам процес парсингу
    conv_res = doc_converter.convert(input_doc_path)
    doc_filename = conv_res.input.file.stem

    # Зберігаємо знайдені картинки як окремі PNG файли
    picture_counter = 0
    for element, _level in conv_res.document.iterate_items():
        if isinstance(element, PictureItem):
            picture_counter += 1
            img_filename = images_dir / f"{doc_filename}_pic_{picture_counter}.png"
            
            # Зберігаємо на диск
            try:
                image_data = element.get_image(conv_res.document)
                if image_data:
                    image_data.save(img_filename, "PNG")
                    
                    # Оновлюємо посилання в елементі на локальний файл
                    if hasattr(element, "image_ref"):
                        element.image_ref = f"./images/{img_filename.name}"
                    elif hasattr(element, "image") and hasattr(element.image, "uri"):
                        element.image.uri = f"./images/{img_filename.name}"
            except Exception as e:
                print(f"Помилка збереження зображення: {e}")

    print(f"Збережено {picture_counter} зображень у папку {images_dir}")

    # Генеруємо чистий Markdown (із посиланнями замість Base64)
    md_output = conv_res.document.export_to_markdown(image_mode=ImageRefMode.REFERENCED)

    md_path = out_dir / f"{doc_filename}.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_output)
        
    print(f"=== ГОТОВО! ===")
    print(f"Markdown файл збережено: {md_path}")

if __name__ == "__main__":
    # Тестовий запуск
    parse_pdf_with_docling("testyvan.pdf", "./output")
