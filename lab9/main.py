#coding:utf8

import unittest
from MovieStore import MovieStore
from DiskFormat import DiskFormat
from DiskMovie import DiskMovie
from TapeMovie import TapeMovie
from TapeFormat import TapeFormat


class TestDiskMovie(unittest.TestCase):
    """Класс тестирования класса фильма на диске"""

    def test_create_empty_barcode(self):
        """Тест создания с пустым штрих-кодом"""
        with self.assertRaises(Exception):
            DiskMovie("", "name", "genre", 100, DiskFormat.DVD)

    def test_create_empty_name(self):
        """Тест создания с пустым именем"""
        with self.assertRaises(Exception):
            DiskMovie("123", "", "genre", 100, DiskFormat.DVD)

    def test_create_success(self):
        """Тест успешного создания"""
        self.assertIsNotNone(DiskMovie("123", "name", "genre", 100, DiskFormat.DVD))

class TestTapeMovie(unittest.TestCase):
    """Класс тестирования класса фильма на кассете"""

    def test_create_empty_barcode(self):
        """Тест создания с пустым штрих-кодом"""
        with self.assertRaises(Exception):
            TapeMovie("", "name", "genre", 100, DiskFormat.DVD)

    def test_create_empty_name(self):
        """Тест создания с пустым именем"""
        with self.assertRaises(Exception):
            TapeMovie("123", "", "genre", 100, DiskFormat.DVD)

    def test_create_success(self):
        """Тест успешного создания"""
        self.assertIsNotNone(TapeMovie("123", "name", "genre", 100, DiskFormat.DVD))

class TestMovieStore(unittest.TestCase):
    def test_duplicate_movies(self):
        """Тест добавления фильмов с повторяющимся штрих-кодом"""
        s = MovieStore()
        
        s.addMovie(DiskMovie("123", "name1", "genre", 100, DiskFormat.MPEG4))

        with self.assertRaises(Exception):
            s.addMovie(DiskMovie("123", "name2", "comedy", 100, DiskFormat.DVD))

    def test_success_adding(self):
        """Тест успешного добавления фильма в хранилище"""
        store = MovieStore()

        store.addMovie(DiskMovie("54354353", "name1", "genre", 100, DiskFormat.MPEG4))
        store.addMovie(DiskMovie("31212312", "name2", "genre", 40, DiskFormat.DVD))

        cnt = len(store.getMovies())

        self.assertEqual(cnt, 2)

    def test_success_disk_dumping(self):
        """Тест успешного сохранения и чтения с диска"""
        store = MovieStore()

        store.addMovie(DiskMovie("54354353", "name1", "genre", 100, DiskFormat.MPEG4))
        store.addMovie(DiskMovie("31212312", "name2", "genre", 40, DiskFormat.DVD))

        store.saveMovies()
        store.loadMovies()

        cnt = len(store.getMovies())

        self.assertEqual(cnt, 2)

if __name__ == "__main__":
    unittest.main()