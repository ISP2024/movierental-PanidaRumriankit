from typing import Collection
from dataclasses import dataclass
import csv


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """
    title: str
    year: int
    genre: Collection[str]

    def get_title(self):
        return self.title

    def is_genre(self, ask_genre):
        for g in self.genre:
            if g.lower() == ask_genre.lower():
                return True
        return False

    def __str__(self):
        return f"{self.title} ({self.year})"


def parse_data():
    data = []
    with open("movies.csv", "r", encoding="UTF-8") as file:
        reader = csv.reader(file)
        for r in reader:
            if r[0] == "#id":
                continue
            data.append(Movie(r[1], int(r[2]), r[3].split("|")))
    return data


class MovieCatalog:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.data = parse_data()

    def get_movie(self, name, year=None):
        for movie in self.data:
            if name == movie.title and not year:
                return movie
            elif name == movie.title and year:
                return movie

