u"""Модуль базового класса фильма."""


class Movie(object):
    u"""Базовый класс фильма."""

    def __init__(self, barcode, name, genre, price):
        u"""Конструктор класса."""
        if len(barcode) == 0:
            raise Exception("Штрих код не может быть пустым")

        if len(name) == 0:
            raise Exception("Имя не может быть пустым")

        self.barcode = barcode
        self.name = name
        self.genre = genre
        self.price = price

    def getBarCode(self):
        u"""Возвращает штрих-код фильма."""
        return self.barcode

    def setPrice(self, price):
        u"""
        Устанавливает новую цену фильма.

        Parameters:
        ----------
        price: integer
            Новая цена

        """
        self.price = price

    def getPrice(self):
        u"""Возвращает цену фильма."""
        return self.price
