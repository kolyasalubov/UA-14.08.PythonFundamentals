class Employee:

    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_info(self):
        print(f"Имя: {self.name}, Зарплата: {self.salary}")

    @classmethod
    def total_employee_count(cls):
        print(f"Total number of employees: {cls.total_employees}")


employee1 = Employee("Vova", 100000)
employee2 = Employee("Olya", 6500)

employee1.display_info()

Employee.total_employee_count()


print(f"Base classes: {Employee.__bases__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"The module in which the class is defined: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")
