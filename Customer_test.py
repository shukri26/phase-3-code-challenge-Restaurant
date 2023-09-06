
from Customer import Customer, Review, Restaurant


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("hamed", "lem")
        self.customer2 = Customer("abdi", "karim")

    def test_given_name(self):
        self.assertEqual(self.customer1.given_name, "hamed")

    def test_family_name(self):
        self.assertEqual(self.customer1.family_name, "lem")

    def test_full_name(self):
        self.assertEqual(self.customer1.full_name(), "hamed lem")

    def test_all(self):
        self.assertEqual(Customer.all(), [self.customer1, self.customer2])

    def test_add_review(self):
        restaurant = Restaurant("Pizza Place")
        self.customer1.add_review(restaurant, 4)
        self.assertEqual(len(Review.all()), 1)
        self.assertEqual(Review.all()[0].customer, self.customer1)
        self.assertEqual(Review.all()[0].restaurant, restaurant)


if __name__ == '__main__':
    unittest.main()
