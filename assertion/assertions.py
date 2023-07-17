class Assertions:

    """Метод проверки наличия блока с ключем"""

    @staticmethod
    def check_block_key(all_block_values, expected_keys):
        for block in all_block_values: # Проходимся по каждому блоку текста в списке
            block_keys = list(block[4].keys()) # Извлекаем ключи из каждого блока со словарем ключ:значений
            if all(key in block_keys for key in expected_keys): # Проверяем наличие всех ожидаемых ключей
                print(f"Блок с ключами {expected_keys} есть в файле.")
                return
        raise AssertionError(f"Ошибка! Блок с ключами {expected_keys} не найден.")

    """Метод проверки расположения блоков"""

    @staticmethod
    def check_block_coordinates(all_block_values, expected_keys, expected_coordinates):
        for block in all_block_values: # Проходим по каждому блоку текста в списке
            # Ищем блок с помощью ключа                          и проверяем, совпадают ли координаты (левая и нижняя)
            if set(expected_keys).issubset(block[4].keys()) and (block[0], block[3]) == expected_coordinates:
                print(f"Блок с ключами {expected_keys} имеет координаты: {expected_coordinates}")
                return
        raise AssertionError(f"Ошибка! Блок с ключами {expected_keys} имеет другие координаты")