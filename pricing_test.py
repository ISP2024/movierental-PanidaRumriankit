import unittest
from pricing import NewRelease, ChildrensPrice, RegularPrice

class TestPriceStrategies(unittest.TestCase):

    def test_new_release_price(self):
        strategy = NewRelease()
        self.assertEqual(strategy.get_price(1), 3)
        self.assertEqual(strategy.get_price(5), 15)

    def test_new_release_rental_points(self):
        strategy = NewRelease()
        self.assertEqual(strategy.get_rental_points(1), 1)
        self.assertEqual(strategy.get_rental_points(5), 5)

    def test_childrens_price(self):
        strategy = ChildrensPrice()
        # Test for 3 days or fewer
        self.assertEqual(strategy.get_price(3), 1.5)
        # Test for more than 3 days
        self.assertEqual(strategy.get_price(5), 4.5)

    def test_childrens_rental_points(self):
        strategy = ChildrensPrice()
        self.assertEqual(strategy.get_rental_points(1), 1)
        self.assertEqual(strategy.get_rental_points(5), 1)

    def test_regular_price(self):
        strategy = RegularPrice()
        # Test for 2 days or fewer
        self.assertEqual(strategy.get_price(2), 2.0)
        # Test for more than 2 days
        self.assertEqual(strategy.get_price(5), 6.5)

    def test_regular_rental_points(self):
        strategy = RegularPrice()
        self.assertEqual(strategy.get_rental_points(1), 1)
        self.assertEqual(strategy.get_rental_points(5), 1)

if __name__ == '__main__':
    unittest.main()
