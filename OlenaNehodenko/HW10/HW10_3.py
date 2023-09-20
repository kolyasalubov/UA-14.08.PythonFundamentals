class Employee:
    total_employees = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1
    
    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
    
    @classmethod
    def display_total_employees(cls):
        print(f"Total Employees: {cls.total_employees}")

# All information about the class and its attributes
print("Base classes:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)
# Creating employees
employee1 = Employee("Irina Adams", 20000)
employee2 = Employee("Mariia Kukla", 10000)

#Individual employee information
employee1.display_info()
employee2.display_info()

#Total number of employees
Employee.display_total_employees()
