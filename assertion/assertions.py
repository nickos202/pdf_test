class Assertions:

    """Метод проверки наличия блока с ключем"""
    @staticmethod
    def check_block_key(all_block_values, expected_keys):
        for block in all_block_values:
            block_keys = list(block[4].keys())
            if all(key in block_keys for key in expected_keys):
                print(f"Блок с ключами {expected_keys} есть в файле.")
                return
        raise AssertionError(f"Ошибка! Блок с ключами {expected_keys} не найден.")

    """Метод проверки расположения блоков"""

    @staticmethod
    def check_block_coordinates(all_block_values, expected_keys, expected_coordinate):
        for block in all_block_values:
            if set(expected_keys).issubset(block[4].keys()) and block[0] == expected_coordinate:
                print(f"Блок с ключами {expected_keys} имеет координату {expected_coordinate}")
                return
        print(f"Ошибка! Блок с ключами {expected_keys} имеет другие координаты")