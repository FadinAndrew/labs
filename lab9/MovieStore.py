u"""Модуль класса хранилища фильмов."""

import json
from DiskFormat import DiskFormat
from DiskMovie import DiskMovie
from TapeMovie import TapeMovie
from TapeFormat import TapeFormat


class MovieStore:
    u"""Класс хранилища фильмов."""

    store = []
    filename = "storedata.txt"

    def __init__(self):
        u"""Конструктор класса."""
        self.store[:] = []

    def addMovie(self, movie):
        u"""
        Добавляет фильм в хранилище.

        Parameters:
        ----------
        movie: Movie
            Фильм
        """
        for m in self.store:
            if m.getBarCode() == movie.getBarCode():
                raise Exception("Такой фильм уже существует")

        self.store.append(movie)

    def getMovie(self, barcode):
        u"""
        Возвращает фильм из хранилища по штрих-коду.

        Parameters:
        ----------
        barcode: string
            Штрих-код
        """
        for m in self.store:
            if m.getBarCode() == barcode:
                return m

    def getMovies(self):
        u"""Возвращает все фильмы."""
        return self.store

    def saveMovies(self):
        u"""Сохраняет все фильмы на диск."""
        with open(self.filename, 'w') as f:
            for m in self.store:
                mt = ""
                # mf = ""
                if type(m) is DiskMovie:
                    mt = "D"
                elif type(m) is TapeMovie:
                    mt = "T"
                else:
                    mt = "U"
                mstr = mt + "|" + m.barcode + "|" + m.name + "|" + m.genre + "|" + str(m.price) + "|" + str(m.format.value) + "\n"
                f.write(mstr)

    def loadMovies(self):
        u"""Загружает все фильмы из диска."""
        self.store[:] = []
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            for l in lines:
                lineData = l.strip("\n").split("|")
                if lineData[0] == "D":
                    dm = DiskMovie(lineData[1], lineData[2], lineData[3], int(lineData[4]), DiskFormat(int(lineData[5])))
                    self.store.append(dm)
                elif lineData[0] == "T":
                    tm = TapeMovie(lineData[1], lineData[2], lineData[3], int(lineData[4]), TapeFormat(int(lineData[5])))
                    self.store.append(tm)
                elif lineData[0] == "U":
                    continue
