class BWT:
    """Класс кодирования и декодирования строки с Burrows-Wheeler transform."""

    @staticmethod
    def append_eom(text: str) -> str:
        return text + '\0'

    @staticmethod
    def encode(text: str) -> (str, int):
        """Метод кодирования строки.

        Метод кодирует строку с помощью Burrows-Wheeler transform.
        Данный метод приводит строку к более удобному для сжатия виду.

        :param text: строка для кодирования
        :return: закодированная строка и позиция для декодирования
        """
        if type(text) is not str:
            raise TypeError(f"Text must be str, not {type(text)}")

        if not text:
            return text

        text = BWT.append_eom(text)

        n: int = len(text)

        # Получаем массив суффиксов переданного текста
        suffixes = [(i, text[i:]) for i in range(n)]
        # Сортируем суффиксы в лексикографическом порядке
        suffixes.sort(key=lambda x: x[1])

        suffix_positions = [i for i, _ in suffixes]
        # Получаем позицию оригинальной строки для декодирования
        position = suffix_positions.index(0)

        bwt_list = []
        for i in range(n):
            # Получаем последний символ i-ого "поворота"
            j = (suffix_positions[i] - 1 + n) % n
            bwt_list.append(text[j])

        bwt_str = ''.join(bwt_list)
        return bwt_str, position

    @staticmethod
    def decode(text: str, position: int) -> str:
        """Метод декодирования строки.

        :param text: закодированная строка
        :param position: позиция при кодировании
        :return: декодированная строка
        """
        if type(text) is not str:
            raise TypeError(f"Text must be str, not {type(text)}")
        if type(position) is not int:
            raise TypeError(f"Text must be str, not {type(position)}")
        if position < 0:
            raise ValueError("Position can't be negative")

        if not text:
            return text

        n: int = len(text)
        sorted_text = sorted(text)

        # Задаём каждому символу позицию в лексикографическом порядке
        symbol_dict: dict[str: int] = {}
        for i in range(n):
            symbol_dict.setdefault(sorted_text[i], len(symbol_dict))

        arr: list[list[int]] = [[] for _ in range(len(symbol_dict))]

        for i in range(n):
            pos = symbol_dict[text[i]]
            arr[pos].append(i)

        # Список предыдущих смещений суффиксов
        prev_shift = [item for sub_arr in arr for item in sub_arr]

        # Нахождение prev_shift
        for i in range(n):
            pos = symbol_dict[sorted_text[i]]
            prev_shift[i] = arr[pos].pop(0)

        decoded = [''] * n
        # Восстановление слова в обратном порядке
        for i in range(n):
            position = prev_shift[position]
            decoded[n - 1 - i] = text[position]

        decoded_str = ''.join(decoded[:0:-1])
        return decoded_str
