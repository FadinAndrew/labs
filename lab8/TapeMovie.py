#coding:utf8

from Movie import Movie

class TapeMovie(Movie):
    """Класс фильма на кассете"""
    def __init__(self, barcode, name, genre, price, format):
        super(TapeMovie, self).__init__(barcode, name, genre, price)
        self.format = format

    def __str__(self):
        return "Tape: {BarCode: " + self.barcode + ", Name: " + self.name + ", Genre: " + self.genre + ", Price: " + str(self.price) + ", Format: " + str(self.format) + "}"

    def __repr__(self):
        return "Tape: {BarCode: " + self.barcode + ", Name: " + self.name + ", Genre: " + self.genre + ", Price: " + str(self.price) + ", Format: " + str(self.format) + "}"