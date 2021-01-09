#coding:utf8

from Movie import Movie
from DiskFormat import DiskFormat

class DiskMovie(Movie):
    """Класс фильма на диске"""
    def __init__(self, barcode, name, genre, price, format):
        super(DiskMovie, self).__init__(barcode, name, genre, price)
        self.format = format

    def __str__(self):
        return "Disk: {BarCode: " + self.barcode + ", Name: " + self.name + ", Genre: " + self.genre + ", Price: " + str(self.price) + ", Format: " + str(self.format) + "}"

    def __repr__(self):
        return "Disk: {BarCode: " + self.barcode + ", Name: " + self.name + ", Genre: " + self.genre + ", Price: " + str(self.price) + ", Format: " + str(self.format) + "}"