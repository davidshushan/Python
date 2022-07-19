from Staff.Worker import Worker
from Enums.Titles import Titles


class Manager(Worker):
    def __init__(self, name, salary):
        super().__init__(name, Titles.Manager.value)
        self.salary = salary

    def get_salary(self):
        return self.salary

    def get_name(self):
        return self.name

    def display(self):
        return "Worker Name : ", self.name, ", Salary: ", self.salary, ", Title: ", self.title
