# Create an employee class. Each employee has characteristics such as name
# and salary. The class should have a counter that calculates the total number of
# employees, as well as a method that prints the total number of employees and a
# method that displays information about each employee in particular, namely the
# name and salary. In addition to creating a class, display information about the base classes from which 
# the employee class is inherited (__base__), the class namespace (__dict__), the 
# class name (__name__), the module name in which the class is defined 
# (__module__), the documentation bar ( __doc__)

class Employee():
    """An employee class"""
    name = ''
    salary = 0
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
        Employee.count = Employee.count + 1

    @staticmethod
    def show_count():
        print('total number of employees:', Employee.count)



    def info(self):
        print ('{:10} | Salary: {} UAH'.format (self.name, self.salary))

#test
e = Employee('Daniil', 30000)
e1 = Employee('Marina', 40000)
e2 = Employee('Varvara', 32000)
e.info()
e1.info()
e2.info()
e2.show_count()
print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)