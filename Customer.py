class Customer:
    
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer._all_customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    classmethod
    def all(cls):
        return cls._all_customers

    def add_review(self, restaurant, rating):
        Review(self, restaurant, rating)


class Review:

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review._all_reviews.append(self)

    def rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls._all_reviews

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant


class Restaurant:
    _all_restaurants = []

    def __init__(self, name):
        self.name = name
        Restaurant._all_restaurants.append(self)

    def name(self):
        return self.name

    @classmethod
    def all(cls):
        return cls._all_restaurants

    def reviews(self):
        return [review for review in Review.all() if review.restaurant == self]

    def customers(self):
        return list({review.customer for review in self.reviews()})

    def average_star_rating(self):
        ratings = [review.rating for review in self.reviews()]
        if ratings:
            return sum(ratings) / len(ratings)
        else:
            return 0
