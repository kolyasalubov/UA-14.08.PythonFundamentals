# Task 3

class Employee:
    employees = []

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employees.append(self)

    @classmethod
    def total_number_of_employees(cls):
        print(f"\nTotal number of employees: {len(cls.employees)}")

    @classmethod
    def input(cls):
        name = input("\nEnter employee name: ")
        salary = float(input("Enter employee salary: "))
        return cls(name, salary)

    @classmethod
    def output(cls):
        for employee in cls.employees:
            print(f"\nName: {employee.name}, \nSalary: {employee.salary}")

while True:
    print("\nMENU")
    print("Enter 1 to add employee")
    print("Enter 2 to see total number of employees")
    print("Enter 3 to print employees")
    print("Enter 4 to exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        employee = Employee.input()
    elif choice == '3':
        employee.output()
    elif choice == '2':
        Employee.total_number_of_employees()
    elif choice == '4':
        break
    else:
        print("\nInvalid choice. Please enter a valid option.")

print("Base classes:", Employee.__bases__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Docstring:", Employee.__doc__)