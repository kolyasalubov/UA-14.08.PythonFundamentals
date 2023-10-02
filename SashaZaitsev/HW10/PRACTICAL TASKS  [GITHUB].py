# 1
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimetr(self):
        return sum(self.sides)

    def area(self):
        raise NotImplementedError("Обчислення площі не реалізовано для базового класу Polygon")

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width, length, width])

    def area(self):
        return self.sides[0] * self.sides[1]
#2
class Human:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Привіт, мене звуть {self.name}."

    @classmethod
    def species_info(cls):
        return "Я належу до роду Homosapiens."

    @staticmethod
    def random_message():
        return "Це повідомлення."
#3
class Employee:

    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_employee_info(self):
        return f"Ім'я: {self.name}, Зарплата: {self.salary}"

    @classmethod
    def print_total_employees(cls):
        return f"Всього робітників: {cls.total_employees}"