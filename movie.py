import logging
from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    _instance = None

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass


class NewRelease(PriceStrategy):
    """Pricing rules for New Release movies."""
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(NewRelease, cls).__new__(cls)
        return cls._instance

    def get_rental_points(self, days):
        """New release rentals earn 1 point for each day rented."""
        return days

    def get_price(self, days) -> float:
        return 3 * days


class ChildrensPrice(PriceStrategy):
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ChildrensPrice, cls).__new__(cls)
        return cls._instance

    def get_rental_points(self, days: int) -> int:
        return 1

    def get_price(self, days) -> float:
        amount = 1.5
        if days > 3:
            amount += 1.5 * (days - 3)
        return amount


class RegularPrice(PriceStrategy):
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(RegularPrice, cls).__new__(cls)
        return cls._instance

    def get_rental_points(self, days: int) -> int:
        return 1

    def get_price(self, days) -> float:
        amount = 2.0
        if days > 2:
            amount += 1.5 * (days - 2)
        return amount


NEW_RELEASE = NewRelease()
REGULAR = RegularPrice()
CHILDREN = ChildrensPrice()


class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code). 
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDRENS = 2
    
    def __init__(self, title, price_code):
        # Initialize a new movie. 
        self.title = title
        self.price_code = price_code
        self.price_strategy = self.get_price_strategy()

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
                f"Movie {self.get_title()} has unrecognized priceCode {self.price_code}")
            raise ValueError(f"Invalid price code: {self.price_code}")

    def get_price_code(self):
        # get the price code
        return self.price_code
    
    def get_title(self):
        return self.title
    
    def __str__(self):
        return self.title

    def get_rental_points(self, days):
        """Delegate the rental points calculation to the price strategy."""
        return self.price_strategy.get_rental_points(days)

    def get_price(self, days):
        """Delegate the price calculation to the price strategy."""
        return self.price_strategy.get_price(days)