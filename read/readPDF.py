import fitz


class ReadPDF:
    @staticmethod
    def read_pdf():
        # file_path = input("Введите путь к файлу: ") # Инпут для чтения файла вне папки source
        file_path = r".\source\test_task.pdf"  # Чтение файла в папки source
        doc = fitz.open(file_path)
        all_block_values = []  # Список всех блоков
        for page in doc:
            output = page.get_text("blocks")  # Создаем переменную с текстовыми блоками
            for block in output:
                block_dict = {}  # Создаем пустой словарь
                block_text = block[4]  # Извлекаем текст из блока
                for pair in block_text.split("\n"):  # Делим текст на строки и сохраняем их в pair
                    if ":" in pair:
                        key, value = pair.split(":", 1)
                        block_dict[key.strip()] = value.strip()  # Добавляем ключ:значение в словарь block_dict
                    else:
                        text = pair.strip()  # Сохраняем текст без ":" как ключ в словарь
                        block_dict[text] = ""
                all_block_values.append((block[0], block[1], block[2], block[3], block_dict, block[5], block[6]))
        return all_block_values

    print(read_pdf())
