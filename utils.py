import os
from pdf2docx import Converter
from docx2pdf import convert
from PIL import Image

def list_files_with_extension(directory, extension):
    return [f for f in os.listdir(directory) if f.endswith(extension)]

def convert_pdf_to_docx(pdf_path, docx_path):
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()

def convert_docx_to_pdf(docx_path, pdf_path):
    convert(docx_path, pdf_path)

def compress_image(image_path, output_path, quality):
    with Image.open(image_path) as img:
        img.save(output_path, optimize=True, quality=quality)

def delete_files_by_pattern(directory, pattern_type, pattern):
    files_to_delete = []
    for file in os.listdir(directory):
        if pattern_type == 'start' and file.startswith(pattern):
            files_to_delete.append(file)
        elif pattern_type == 'end' and file.endswith(pattern):
            files_to_delete.append(file)
        elif pattern_type == 'contain' and pattern in file:
            files_to_delete.append(file)
        elif pattern_type == 'extension' and file.endswith(pattern):
            files_to_delete.append(file)

    for file in files_to_delete:
        os.remove(os.path.join(directory, file))
        print(f"Файл: \"{file}\" успешно удалён!")