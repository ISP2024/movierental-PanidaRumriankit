import re
import unittest 
from customer import Customer
from rental import Rental
from movie import Movie

class CustomerTest(unittest.TestCase): 
    """ Tests of the Customer class"""
    
    def setUp(self):
        """Test fixture contains:

        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", Movie.NEW_RELEASE)
        self.regular_movie = Movie("CitizenFour", Movie.REGULAR)
        self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)

    @unittest.skip("No convenient way to test")
    def test_billing():
        # no convenient way to test billing since its buried in the statement() method.
        pass
    
    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4)) # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])

    def test_total_amount(self):
        rental1 = Rental(self.new_movie, 2)
        rental2 = Rental(self.regular_movie, 2)
        rental3 = Rental(self.childrens_movie, 5)
        self.c.add_rental(rental1)
        self.c.add_rental(rental2)
        self.c.add_rental(rental3)
        self.assertEqual(self.c.total_amount(), 12.5)

    def test_total_renter_points(self):
        rental1 = Rental(self.new_movie, 2)
        rental2 = Rental(self.regular_movie, 2)
        rental3 = Rental(self.childrens_movie, 5)
        self.c.add_rental(rental1)
        self.c.add_rental(rental2)
        self.c.add_rental(rental3)
        self.assertEqual(self.c.frequent_renter_points(), 4)

