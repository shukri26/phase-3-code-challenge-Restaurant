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
