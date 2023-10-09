class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @staticmethod
    def name_count():
        print(f'Employees: {Employee.count}')

    def info(self):
        print(f'Name: {self.name}, Salary: {self.salary} UAH')


exp1 = Employee('Oleksii', 83435)
exp1.info()
exp1.name_count()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
