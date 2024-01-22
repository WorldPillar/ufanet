from archiving import RLE
from archiving import BWT


class Archiver:
    """Класс архивации и расшифорвки строки."""

    @staticmethod
    def archiver(text: str, bwt: bool = True) -> str:
        """Метод сжатия строки.

        :param text: строка для сжатия
        :param bwt: использование bwt
        :return: сжатая строка
        """
        result = RLE.encode(text)

        result_bwt = text
        if bwt:
            result_bwt, position = BWT.encode(text)
            result_bwt = RLE.encode(result_bwt)
            result_bwt = str(position) + result_bwt

        if bwt and len(result_bwt) < len(result):
            return result_bwt

        return result

    @staticmethod
    def unpacker(text: str) -> str:
        """Метод распаковки строки.

        :param text: строка для распаковки
        :return: распакованная строка
        """
        result = text

        position = -1
        bwt_encoded = False

        if text[0].isdigit():
            bwt_encoded = True
            position = 0
            i = 0
            while text[i].isdigit():
                position = position * 10 + int(text[i])
                i += 1
            result = text[i:]

        result = RLE.decode(result)

        if bwt_encoded:
            result = BWT.decode(result, position)

        return result
