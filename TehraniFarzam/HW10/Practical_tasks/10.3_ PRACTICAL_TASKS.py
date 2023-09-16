class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = float(salary)
        Employee.total_employees += 1

    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary}."
        

    @classmethod
    def print_total_employees(cls):
        print(f"Total Employees: {cls.total_employees}")

employees = []

while True:
    name = input("Enter employee name (or 'quit' to exit): ").capitalize()

    if name.lower() == 'quit':
        break
    salary = input("Enter employee salary: ")

    employee = Employee(name, salary)
    employees.append(employee)


for employee in employees:
    print(employee.display_info())

Employee.print_total_employees()

# Display class-level information  
print("Base Classes:", Employee.__bases__)
print("Class Namespace:", Employee.__dict__)
print("Class Name:", Employee.__name__)
print("Module Name:", Employee.__module__)
print("Documentation:", Employee.__doc__)