from Client.Client import Client
from Meals.Meal import Meal
from Resturant.Restaurant import Restaurant
from Staff.Manager import Manager as Manager
from Staff.Worker import Worker
from Order.Order import Order

def remove_meal(meals_list):
    res = choose_meal(meals_list)
    meals_list.remove(res)
    return meals_list


def begining() -> Manager:
    print("Welcome! \n Please enter new Manager Details:")
    name = input("Enter Manager name: \n")
    # todo validation on input and default case
    salary: int = input("Enter Manager Salary: \n")
    manager = Manager(name, salary)
    return manager

def add_meal() -> Meal:
    meal_name = input("Enter Meal name: \n")
    meal_price: int = input("Enter Meal Price: \n")
    new_meal = Meal(meal_name, meal_price)
    return new_meal

def add_worker() -> Worker:
    worker_name = input("Enter Worker name: \n")
    worker_salary: int = input("Enter Worker salary: \n")
    new_worker = Worker(worker_name, worker_salary)
    return new_worker

def pay(order):
    print("check out...")
    print("your order is: ")
    # display_list(order.mealList)

    order.print_meals()
    flag = True
    while flag:
        print("""
        (1) pay
        (2) remove meal from list
        """)
        res = int(input())
        if res == 2:
            order.mealList = remove_meal(order.mealList)

        else: flag = False

    print("thank you: ", order.Client.name, " Until next time...")
    sum = order.Bill()
    return sum

def display_list(list):
    print("list:")
    for x in range(len(list)):

        print("(", (x + 1), ")  ",list[x].display() )

def choose_meal(meals_list)->Meal:
    flag = True
    while flag:
        print("type a meal number from the list: \n")
        # display_list(meals_list)

        for x in range(len(meals_list)):
            print("(",(x + 1),")  ", meals_list[x].name, "-------- price: ",  meals_list[x].price)
        res = int(input())
        # todo validate res to be int
        if (res <= len(meals_list)):
            res = meals_list[res - 1]
            return res


def choose_worker(workers_list)->Worker:
    flag = True
    while flag:
        print("type a worker number from the list:")
        for x in workers_list:
            print("(",(workers_list.index(x) + 1), ")  worker", x.name, "-------- worker title: ", x.title)
        print("type here... ")
        res = int(input())
        # todo validate res to be int
        if (res <= len(workers_list)):
            res = workers_list[res - 1]
            return res

def choose_order(orders_list)->Order:
    flag = True
    while flag:
        print("type an order number from the list: \n")
        # for x in orders_list:
        #     print("(",(orders_list.index(x) + 1), ")  order", x.display())
        display_list(orders_list)
        print("type here... \n")
        res = int(input())
        # todo validate res to be int
        if (res <= len(orders_list)):
            res = orders_list[res - 1]
            return res




def Meals():
    print("Please enter First Meal: \n")
    meals_list = []
    meals_list.append(add_meal())

    ans = True
    while ans:

        print("""
        What would you like to do? \n
           1.Add a Meal
           2.Show meals list
           3.Exit/Quit
           """)
        ans = input()
        if ans == "1":
            meals_list.append(add_meal())
        elif ans == "2":
            display_list(meals_list)
        else:
            ans = False
    return meals_list


def menu():
    print("creating a new restaurant...")
    manager = begining()
    workers = []
    workers.append(manager)
    # display_list(workers)
    orders = []
    meals_list = Meals()
    restaurant = Restaurant(orders, workers, meals_list)

    ans = True
    while ans:
        print("""
        1.Show workers list
        2.add a worker
        3.delete a worker
        4.get a new Order
        5.Show Orders list
        6.Show current benefit
        7.Show Payed benefit      
        8.pay Order
        9.Exit/Quit
        """)
        ans = input("What would you like to do? \n")
        if ans == "1":
            display_list(restaurant.Workers)
        elif ans == "2":
            restaurant.add_worker(add_worker())
        elif ans == "3":
            restaurant.remove_worker(choose_worker(restaurant.Workers))
        elif ans == "4":
            restaurant.add_order(new_order(restaurant.Workers, restaurant.Meals))
        elif ans == "5":
            # display_list(restaurant.Orders)
            restaurant.display_orders()
        elif ans == "6":
            restaurant.current_benefit()
            print("current benefit is:", restaurant.Benefit)
        elif ans == "7":
            print("the payed benefit of the restaurant is:",restaurant.Payed)
        elif ans == "8":
            order_to_remove = choose_order(restaurant.Orders)
            restaurant.Payed = pay(order_to_remove)
            restaurant.remove_order(order_to_remove)

        elif ans == "9":
            ans = False
            print("\n Goodbye")
        elif ans != "":
            print("\n Not Valid Choice Try again")


def new_order(workers: [], meals: [])->Order:
    print("New Order: \n")
    client_name = input("Enter Client Name: \n")
    client_age: int = input("Enter Client age: \n")
    # todo: display meals list and choose 1 of them

    # todo validate age to be int
    worker = choose_worker(workers)
    client = Client(client_name, client_age)

    order = Order(client, worker) # create a new order

    # order.add_Meal()
    flag = True
    while flag:
        order.add_Meal(choose_meal(meals))
        print("(1) add a meal")
        print("(2) continue")
        res = int(input())
        if res == 2:
            flag = False
    return order







if __name__ == "__main__":
    menu()
    # begining()

    # choose_meal(Meals())
    # w = Waiter("aaa", 100)
    # m = Manager("bbb", 200)
    # h = Hostess("ccc", 300)
    # list = [w,m,h]
    # display_list(list)

