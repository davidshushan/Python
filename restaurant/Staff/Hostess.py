from Staff.Worker import Worker
from Enums.Titles import Titles


class Hostess(Worker):
    def __init__(self, name, salary):
        super().__init__(name, Titles.Hostess.value)
        self.salary = salary


    def get_salary(self):
        return self.salary


    def get_name(self):
        return self.name
