#coding:utf8

class Movie(object):
    """Базовый класс фильма"""
    def __init__(self, barcode, name, genre, price):
        if len(barcode) == 0:
            raise Exception("Штрих код не может быть пустым")

        if len(name) == 0:
            raise Exception("Имя не может быть пустым")

        self.barcode = barcode
        self.name = name
        self.genre = genre
        self.price = price

    def getBarCode(self):
        """
        Возвращает штрих-код фильма

        """
        return self.barcode
    
    def setPrice(self, price):
        """
        Устанавливает новую цену фильма

        Parameters:
        ----------
        price: integer
            Новая цена
        """
        self.price = price

    def getPrice(self):
        """
        Возвращает цену фильма
        """
        return self.price

    def __str__(self):
        return self.barcode