import unittest
from Review import Review, Customer, Restaurant


class TestReview(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("John", "Doe")
        self.restaurant1 = Restaurant("Burger King")

    def test_rating(self):
        review1 = Review(self.customer1, self.restaurant1, 4)
        self.assertEqual(review1.rating, 4)

    def test_all(self):
        review1 = Review(self.customer1, self.restaurant1, 4)
        self.assertEqual(Review.all(), [review1])

    def test_customer(self):
        review1 = Review(self.customer1, self.restaurant1, 4)
        self.assertEqual(review1.customer, self.customer1)

    def test_restaurant(self):
        review1 = Review(self.customer1, self.restaurant1, 4)
        self.assertEqual(review1.restaurant, self.restaurant1)


if __name__ == '__main__':
    unittest.main()
