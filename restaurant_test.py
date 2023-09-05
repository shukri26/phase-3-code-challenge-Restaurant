import unittest
from Restaurant import Restaurant, Review, Customer


class TestRestaurant(unittest.TestCase):

    def setUp(self):
        self.restaurant1 = Restaurant("Burger King")
        self.restaurant2 = Restaurant("Pizza Hut")
        self.customer1 = Customer("John", "Doe")

    def test_name(self):
        self.assertEqual(self.restaurant1.name, "Burger King")

    def test_all(self):
        self.assertEqual(Restaurant.all(), [self.restaurant1, self.restaurant2])

    def test_reviews(self):
        review1 = Review(self.customer1, self.restaurant1, 4)
        review2 = Review(self.customer1, self.restaurant2, 5)
        self.assertEqual(self.restaurant1.reviews(), [review1])

    def test_customers(self):
        review1 = Review(self.customer1, self.restaurant1, 4)
        review2 = Review(self.customer1, self.restaurant2, 5)
        self.assertEqual(self.restaurant1.customers(), [self.customer1])

    def test_average_star_rating(self):
        review1 = Review(self.customer1, self.restaurant1, 4)
        review2 = Review(self.customer1, self.restaurant1, 5)
        self.assertEqual(self.restaurant1.average_star_rating(), 4.5)


if __name__ == '__main__':
    unittest.main()
