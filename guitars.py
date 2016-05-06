class Guitars:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        age = 2016 - self.year
        return age

    def is_vintage(self):
        is_vintage = True
        if self.get_age() <50:
            is_vintage = False
            return is_vintage
        return is_vintage

    def __str__(self, name):
        return self.name
