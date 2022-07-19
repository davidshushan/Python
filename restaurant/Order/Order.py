
class Order:
    count = 0

    def __init__(self, Client, Worker):
        self.Worker = Worker
        self.Client = Client
        self.orderId = Order.count + 1
        self.sum = 0.0
        self.mealList = []

    def display(self):
        # self.Client.display()
        # self.print_meals()
        # print(self.Worker.display())
        self.set_sum()
        return "order id is: ", self.orderId, " Client Name: ", self.Client.name, "  age: ", self.Client.age, \
                "Worker Name: ", self.Worker.name, ", Worker title: ", self.Worker.title, ", sum is: ", self.sum

    def print_meals(self):
        for string in self.mealList:
            print(str(string))

    def OrderBill(self):
        res = self.Client.Bill()
        return res

    def set_sum(self):
        self.sum = self.Bill()

    def add_Meal(self, Meal):
        self.mealList.append(Meal)

    def remove_Meal(self, Meal):
        self.mealList.remove(Meal)

    def Bill(self):
        res = 0
        for item in self.mealList:
            x = int(item.price)
            res = res + x
        return res

    def Payed(self):
        res = self.sum
        self.sum = 0.0
        return res
