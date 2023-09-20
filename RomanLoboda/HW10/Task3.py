class Employee:
    """
    display name and salary of employee
    """
    emp_counter = 0

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        Employee.emp_counter += 1

    def get_employee(self):
        return f"Employee : {self.__name}, Salary is {self.__salary}"

    @classmethod
    def number_employee(cls):
        return f"The total number of employee : {cls.emp_counter}"

    def set_salary(self, salary):
        if 0<salary<10000:
            self.__salary=salary
        else:
            print("Salary can not be bigger then 10000 or less then 0")




employee1=Employee("Roma", 2000)
employee2=Employee("Artem", 3000)
employee3=Employee("Max", 1000)

print(employee1.get_employee())
print(employee2.get_employee())
print(employee3.get_employee())
print(Employee.number_employee())

employee1._Employee__salary=6000
print(employee1.get_employee())

employee2.set_salary(9000)
print(employee2.get_employee())

employee3.set_salary(19000)
print(employee3.get_employee())



# print("Base Classes:", Employee.__bases__)
# print("Class Namespace:", Employee.__dict__)
# print("Class Name:", Employee.__name__)
# print("Module Name:", Employee.__module__)
# print("Documentation:", Employee.__doc__)
