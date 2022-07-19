from abc import ABC, abstractmethod

class Worker(ABC):

    def __init__(self, name, title):
        self.name = name
        self.title = title

    def display(self):
        return "Worker Name : ", self.name, ", Title: ", self.title

        @abstractmethod
        def get_name(self):
            pass

        @abstractmethod
        def get_salary(self):
            pass
