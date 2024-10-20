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
