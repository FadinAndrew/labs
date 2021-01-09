u"""Модуль класса фильма на диске."""

from Movie import Movie
from DiskFormat import DiskFormat


class DiskMovie(Movie):
    u"""Класс фильма на диске."""

    def __init__(self, barcode, name, genre, price, format):
        u"""Конструктор класса."""
        super(DiskMovie, self).__init__(barcode, name, genre, price)
        self.format = format

    def __str__(self):
        u"""Метод строкового представления."""
        return "Disk: {BarCode: " + self.barcode + ", Name: " + self.name + ", Genre: " + self.genre + ", Price: " + str(self.price) + ", Format: " + str(self.format) + "}"

    def __repr__(self):
        u"""Для отладки."""
        return "Disk: {BarCode: " + self.barcode + ", Name: " + self.name + ", Genre: " + self.genre + ", Price: " + str(self.price) + ", Format: " + str(self.format) + "}"
