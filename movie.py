from typing import Collection
from dataclasses import dataclass


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
