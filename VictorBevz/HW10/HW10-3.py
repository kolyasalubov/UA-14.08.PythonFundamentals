class Employee:
    employees_amount = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = int(salary)
        Employee.employees_amount += 1
    def info(self):
        return f"Name: {self.name}\n Salary: {self.salary}"
     
    @classmethod
    def print_total_employees(amount):
        print(f"Amount of employees: {amount.employees_amount}")
        
total = []   
while True:
    name = input("Input employee's name(type 's' to stop providing information)->").capitalize()
    if name.lower() == "s":
        break
    salary = input("Input employee's salary->")
    employee = Employee(name, salary)
    total.append(employee)
    
for employee in total:
    print(employee.info())

Employee.print_total_employees()