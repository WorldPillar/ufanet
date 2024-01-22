class RLE:
    """Класс архивации и расшифровки строки методом Run-Length Encoding."""

    @staticmethod
    def __escaping(char: str) -> str:
        """Метод экранирования цифры или '/'.

        :param char: символ для экранирования
        :return: экранированный символ
        """
        if char.isdigit():
            char = f'/{char}'
        elif char == '/':
            char = '//'

        return char

    @staticmethod
    def encode(text: str) -> str:
        """Метод для архивации данных.

        Метод сжимает строку, заменяя серию повторяющихся символов
        на один символ и число повторов. Например, AAA -> A3.

        :param text: строка для сжатия
        :return: "сжатая" строка
        """
        if type(text) is not str:
            raise TypeError(f"Text must be str, not {type(text)}")

        if not text:
            return text

        result: list[str] = []
        count: int = 1

        for i in range(len(text) - 1):
            if text[i] == text[i + 1]:
                count += 1
            else:
                char = RLE.__escaping(text[i])

                res = f'{char}' if count == 1 else f'{char}{count}'
                result.append(res)

                count = 1

        char = RLE.__escaping(text[-1])

        res = f'{char}' if count == 1 else f'{char}{count}'
        result.append(res)

        archive_text: str = ''.join(result)
        return archive_text

    @staticmethod
    def decode(text: str) -> str:
        """Метод для разархивирования данных.

        :param text: "сжатая" строка
        :return: исходная строка
        """
        if type(text) is not str:
            raise TypeError(f"Text must be str, not {type(text)}")

        if not text:
            return text

        result: list[str] = []
        i: int = 0

        while i < len(text):
            char: str = text[i]
            count: int = 0

            i += 1
            # При обнаружении экранирования смещаемся на нужный символ
            if char == '/' and (text[i].isdigit() or text[i] == '/'):
                char = text[i]
                i += 1

            while i < len(text) and text[i].isdigit():
                count = count * 10 + int(text[i])
                i += 1

            result.append(char * max(count, 1))

        unpack_text: str = ''.join(result)
        return unpack_text
