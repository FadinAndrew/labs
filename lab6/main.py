#coding:utf8

from MovieStore import MovieStore
from DiskFormat import DiskFormat
from DiskMovie import DiskMovie
from TapeMovie import TapeMovie
from TapeFormat import TapeFormat

def main():
    s = MovieStore()

    m1 = DiskMovie("1234324324", "Breaking Bad", "Action", 100, DiskFormat.HD_DVD)
    s.addMovie(m1)

    m2 = DiskMovie("84835834532", "Fast & Furious", "Action", 150, DiskFormat.DVD)
    s.addMovie(m2)

    m3 = TapeMovie("88324454353", "The Hangover", "Comedy", 200, TapeFormat.VHS)
    s.addMovie(m3)

    s.saveMovies()
    s.loadMovies()

    allMovies = s.getMovies()
    print(allMovies)

if __name__ == "__main__":
    main()