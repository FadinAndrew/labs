# coding=utf8
from enum import Enum

class NumberFormat(Enum):
    """Перечисление типов возвращаемого значения"""

    DEC = 1 #Десятичный
    BIN = 2 #Бинарный
    FULLBIN = 3 #Бинарный с ведущими нулями

class OverflowException(Exception):
    """Возникает при переполнении двоичного числа"""
    def __init__(self, message):
        super(OverflowException, self).__init__(message)

class BinaryNumber:
    """Класс двоичного представления числа"""
    def __init__(self, n):
        """
        Конструктор

        Parameters:
        ----------
        n: number
            Число разрядов
        """
        self.n = n

    def setNumber(self, num):
        """
        Метод устанавливает число, которое будет  представлено в двоичном виде

        Parameters:
        ----------
        num: number
            Число, которое надо представить в двоичном виде
        """
        maxNum = 2 ** self.n - 1
        if maxNum < num:
            raise OverflowException("Число " + str(num)  + " превышает максимальное количество разрядов")
        self.num = num

    def getNumber(self, nf = NumberFormat.DEC):
        """
        Возвращает строковое представление числа

        Parameters:
        ----------
        nf: NumberFormat
            Тип представления
        """
        if nf is NumberFormat.DEC:
            return str(self.num)
        if nf is NumberFormat.BIN:
            return "{0:b}".format(self.num)
        if nf is NumberFormat.FULLBIN:
            binNum = "{0:b}".format(self.num)
            binLen = len(binNum)
            z = self.n - binLen
            leadingZeroes = "0" * z
            return leadingZeroes + binNum

def main():
    bd = BinaryNumber(8)
    try:
        bd.setNumber(256)
        print(bd.getNumber(NumberFormat.FULLBIN))
    except OverflowException as e:
        print('Ошибка: ' + str(e))


if __name__ == "__main__":
    main()