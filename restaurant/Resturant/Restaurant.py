# from restaurant.Client.Client import Client
# from restaurant.Staff.Manager import Manager
# from restaurant.Staff.Hostess import Hostess
# from restaurant.Meals.Meal import Meal as Meal


class Restaurant:
    def __init__(self, orders, workers, meals):
        self.Orders = orders
        self.Workers = workers
        self.Benefit = 0.0
        self.Payed = 0.0
        self.Meals = meals

    def display_Resturant(self):
        self.display_orders()
        self.display_workers()
        print("Benefit:", self.Benefit)

    def display_orders(self):
        for i in  self.Orders:
            i.display()

    def display_workers(self):
        for i in range(0, len(self.Workers)):
            print(self.Workers[i])

    def current_benefit(self):
        benefit = 0.0
        for i in self.Orders:
            benefit = benefit + i.sum
        self.Benefit = benefit



    def add_worker(self, worker):
        self.Workers.append(worker)

    def remove_worker(self, worker):
        self.Workers.remove(worker)


    def add_order(self, order):
        self.Orders.append(order)

    def remove_order(self, order):
        self.Orders.remove(order)

    def add_meal(self, meal):
        self.meals.append(meal)

    def remove_meal(self, meal):
        self.meals.remove(meal)




# if __name__ == '__main__':
#     c1 = Client("John", 36)
#     m1 = Meal("Pizza", 36)
#     m2 = Meal("donates", 10)
#     c1.addMeal(m1)
#     c1.addMeal(m2)
#
#     c2 = Client("jessi", 25)
#     c2.addMeal(m1)
#     c2.addMeal(m2)
#     clients = [c1, c2]
#     m1 = Manager("maor", 22)
#     h1 = Hostess("david", 24)
#     workers = [m1, h1]
#
#     r1 = Restaurant(workers, clients)
#     r1.display_Resturant()
