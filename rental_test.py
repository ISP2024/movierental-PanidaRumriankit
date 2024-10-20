import unittest
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):
    
    def setUp(self):
        self.new_movie = Movie("Dune: Part Two")
        self.regular_movie = Movie("Air")
        self.childrens_movie = Movie("Frozen")

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air")
        self.assertEqual("Air", m.get_title())

    @unittest.skip("add this test when you refactor rental price")
    def test_rental_price(self):
        rental = Rental(self.new_movie, 1, Rental.NEW_RELEASE)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5, Rental.NEW_RELEASE)
        self.assertEqual(rental.get_price(), 15.0)
        self.fail("TODO add more tests for other movie categories")

    def test_rental_points(self):
        rental = Rental(self.new_movie, 5, Rental.NEW_RELEASE)
        self.assertEqual(rental.get_rental_points(), 5)
        rental = Rental(self.new_movie, 1, Rental.NEW_RELEASE)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.regular_movie, 5, Rental.REGULAR)
        self.assertEqual(rental.get_rental_points(), 1)
