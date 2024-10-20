import unittest
from rental import Rental
from movie import Movie, MovieCatalog


class RentalTest(unittest.TestCase):
    
    def setUp(self):
        all_movie = MovieCatalog()
        self.new_movie = all_movie.get_movie(name="Dune: Part Two")
        self.regular_movie = all_movie.get_movie(name="Sound of Freedom")
        self.childrens_movie = all_movie.get_movie(name="Cinderella")

    # def test_movie_attributes(self):
    #     """trivial test to catch refactoring errors or change in API of Movie"""
    #     m = Movie("Air")
    #     self.assertEqual("Air", m.get_title())

    def test_rental_price(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)
        rental = Rental(self.regular_movie, 1)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 5)
        self.assertEqual(rental.get_price(), 6.5)
        rental = Rental(self.childrens_movie, 2)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 4)
        self.assertEqual(rental.get_price(), 3.0)
        # self.fail("TODO add more tests for other movie categories")

    def test_rental_points(self):
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_rental_points(), 5)
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.regular_movie, 5)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.childrens_movie, 5)
        self.assertEqual(rental.get_rental_points(), 1)
