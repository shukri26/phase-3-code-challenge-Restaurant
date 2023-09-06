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
