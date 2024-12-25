import os
import utils

def display_menu():
    print("Выберите действие:")
    print("0. Сменить рабочий каталог")
    print("1. Преобразовать PDF в Docx")
    print("2. Преобразовать Docx в PDF")
    print("3. Произвести сжатие изображений")
    print("4. Удалить группу файлов")
    print("5. Выход")

def change_directory():
    new_directory = input("Укажите корректный путь к рабочему каталогу: ")
    if os.path.isdir(new_directory):
        os.chdir(new_directory)
        print(f"Текущий каталог: {os.getcwd()}")
    else:
        print("Указанный путь не является каталогом.")

def convert_pdf_to_docx_menu():
    pdf_files = utils.list_files_with_extension(os.getcwd(), '.pdf')
    if not pdf_files:
        print("В текущем каталоге нет файлов с расширением .pdf.")
        return

    print("Список файлов с расширением .pdf в данном каталоге:")
    for i, file in enumerate(pdf_files, start=1):
        print(f"{i}. {file}")

    choice = input("Введите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0): ")
    if choice == '0':
        for pdf_file in pdf_files:
            docx_file = pdf_file.replace('.pdf', '.docx')
            utils.convert_pdf_to_docx(pdf_file, docx_file)
            print(f"Файл {pdf_file} успешно преобразован в {docx_file}")
    else:
        try:
            index = int(choice) - 1
            if 0 <= index < len(pdf_files):
                pdf_file = pdf_files[index]
                docx_file = pdf_file.replace('.pdf', '.docx')
                utils.convert_pdf_to_docx(pdf_file, docx_file)
                print(f"Файл {pdf_file} успешно преобразован в {docx_file}")
            else:
                print("Неверный номер файла.")
        except ValueError:
            print("Неверный ввод.")

def convert_docx_to_pdf_menu():
    docx_files = utils.list_files_with_extension(os.getcwd(), '.docx')
    if not docx_files:
        print("В текущем каталоге нет файлов с расширением .docx.")
        return

    print("Список файлов с расширением .docx в данном каталоге:")
    for i, file in enumerate(docx_files, start=1):
        print(f"{i}. {file}")

    choice = input("Введите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0): ")
    if choice == '0':
        for docx_file in docx_files:
            pdf_file = docx_file.replace('.docx', '.pdf')
            utils.convert_docx_to_pdf(docx_file, pdf_file)
            print(f"Файл {docx_file} успешно преобразован в {pdf_file}")
    else:
        try:
            index = int(choice) - 1
            if 0 <= index < len(docx_files):
                docx_file = docx_files[index]
                pdf_file = docx_file.replace('.docx', '.pdf')
                utils.convert_docx_to_pdf(docx_file, pdf_file)
                print(f"Файл {docx_file} успешно преобразован в {pdf_file}")
            else:
                print("Неверный номер файла.")
        except ValueError:
            print("Неверный ввод.")

def compress_images_menu():
    image_files = []
    for extension in ('.jpeg', '.gif', '.png', '.jpg'):
        image_files.extend(utils.list_files_with_extension(os.getcwd(), extension))

    if not image_files:
        print("В текущем каталоге нет файлов с расширениями ('.jpeg', '.gif', '.png', '.jpg').")
        return

    print("Список файлов с расширениями ('.jpeg', '.gif', '.png', '.jpg') в данном каталоге:")
    for i, file in enumerate(image_files, start=1):
        print(f"{i}. {file}")

    choice = input("Введите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0): ")
    if choice == '0':
        quality = int(input("Введите параметры сжатия (от 0 до 100%): "))
        for image_file in image_files:
            compressed_file = image_file.replace('.jpg', '_compressed.jpg').replace('.jpeg', '_compressed.jpeg').replace('.png', '_compressed.png').replace('.gif', '_compressed.gif')
            utils.compress_image(image_file, compressed_file, quality)
            print(f"Файл {image_file} успешно сжат в {compressed_file}")
    else:
        try:
            index = int(choice) - 1
            if 0 <= index < len(image_files):
                image_file = image_files[index]
                quality = int(input("Введите параметры сжатия (от 0 до 100%): "))
                compressed_file = image_file.replace('.jpg', '_compressed.jpg').replace('.jpeg', '_compressed.jpeg').replace('.png', '_compressed.png').replace('.gif', '_compressed.gif')
                utils.compress_image(image_file, compressed_file, quality)
                print(f"Файл {image_file} успешно сжат в {compressed_file}")
            else:
                print("Неверный номер файла.")
        except ValueError:
            print("Неверный ввод.")

def delete_files_menu():
    print("Выберите действие:")
    print("1. Удалить все файлы начинающиеся на определенную подстроку")
    print("2. Удалить все файлы заканчивающиеся на определенную подстроку")
    print("3. Удалить все файлы содержащие определенную подстроку")
    print("4. Удалить все файлы по расширению")

    choice = input("Введите номер действия: ")
    if choice == '1':
        pattern_type = 'start'
    elif choice == '2':
        pattern_type = 'end'
    elif choice == '3':
        pattern_type = 'contain'
    elif choice == '4':
        pattern_type = 'extension'
    else:
        print("Неверный выбор.")
        return

    pattern = input("Введите подстроку: ")
    utils.delete_files_by_pattern(os.getcwd(), pattern_type, pattern)

def main():
    while True:
        print(f"Текущий каталог: {os.getcwd()}")
        display_menu()
        choice = input("Ваш выбор: ")
        if choice == '0':
            change_directory()
        elif choice == '1':
            convert_pdf_to_docx_menu()
        elif choice == '2':
            convert_docx_to_pdf_menu()
        elif choice == '3':
            compress_images_menu()
        elif choice == '4':
            delete_files_menu()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте ещё раз.")

if __name__ == "__main__":
    main()