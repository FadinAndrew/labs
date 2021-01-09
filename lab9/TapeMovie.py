u"""Модуль класса фильма на кассете."""

from Movie import Movie


class TapeMovie(Movie):
    u"""Класс фильма на кассете."""

    def __init__(self, barcode, name, genre, price, format):
        u"""Конструктор класса."""
        super(TapeMovie, self).__init__(barcode, name, genre, price)
        self.format = format

    def __str__(self):
        u"""Метод строкового представления."""
        return "Tape: {BarCode: " + self.barcode + ", Name: " + self.name + ", Genre: " + self.genre + ", Price: " + str(self.price) + ", Format: " + str(self.format) + "}"

    def __repr__(self):
        u"""Для отладки."""
        return "Tape: {BarCode: " + self.barcode + ", Name: " + self.name + ", Genre: " + self.genre + ", Price: " + str(self.price) + ", Format: " + str(self.format) + "}"
