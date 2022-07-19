class Meal:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"  {self.name}, price is {self.price}"

    def display(self):
        return f"  {self.name}, price is {self.price}"
