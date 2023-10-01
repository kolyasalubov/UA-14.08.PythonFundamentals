class Employee():
    """Employee class, Saves employee information: name, salary, number of employees"""
    employees_counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employees_counter += 1

    def number_of_employees():
        print(f"The number of all employees: {Employee.employees_counter}")

    def show_employee(self):
       print(f"Employee: {self.name}, salary: {self.salary}")

    def __del__(self):
        Employee.employees_counter -= 1

bill = Employee("Bill Steckman", 4500)
tedd = Employee("Tedd Wilson", 3800)
stiv = Employee("Stiv Jonson", 145000)

Employee.number_of_employees()
tedd.show_employee()
stiv.show_employee()
bill.show_employee()

del bill
Employee.number_of_employees()

print("\n======================================================")
print("About class Employee:\t", Employee.__mro__)
print("The class namespace:\t", Employee.__dict__)
print("The class name:\t", Employee.__name__)
print("The module name in which the class is defined:\t", Employee.__module__)
print("The documentation bar:\t", Employee.__doc__)
