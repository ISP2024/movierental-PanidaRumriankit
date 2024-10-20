import logging
from movie import Movie
from pricing import NEW_RELEASE, CHILDREN, REGULAR
import datetime


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """

    # The types of movies (price_code).
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDRENS = 2
    
    def __init__(self, movie, days_rented):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = self.price_code_for_movie()
        self.price_strategy = self.get_price_strategy()

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_price_code(self):
        # get the price code
        return self.price_code

    def price_code_for_movie(self):
        if self.movie.year == datetime.datetime.year:
            return self.NEW_RELEASE
        elif "Children" in self.movie.genre or "Childrens" in self.movie.genre:
            return self.CHILDRENS
        else:
            return self.REGULAR

    def get_price_strategy(self):
        """Return the appropriate PriceStrategy based on the price_code."""
        if self.price_code == self.NEW_RELEASE:
            return NEW_RELEASE
        elif self.price_code == self.CHILDRENS:
            return CHILDREN
        elif self.price_code == self.REGULAR:
            return REGULAR
        else:
            log = logging.getLogger()
            log.error(
                f"Movie {self.movie.get_title()} has unrecognized priceCode {self.movie.price_code}")
            raise ValueError(f"Invalid price code: {self.movie.price_code}")

    def get_price(self) -> float:
        return self.price_strategy.get_price(self.days_rented)

    def get_rental_points(self):
        return self.price_strategy.get_rental_points(self.days_rented)


