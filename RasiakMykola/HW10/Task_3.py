
# 10.3 PRACTICAL TASKS / [GITHUB]

# Task 3
class Employee:
    '''
    Create an employee class.
    '''
    
    def __init__(self, counter, name_salary):
        self.counter = counter
        self.name_salary = name_salary

    def total_number_of_employees (self):
        print(f"\nThe total number of employees is {self.counter}")
        
    
    def info_about_employees(self):
        print('\n')
        print('   ')
        for name, salary in self.name_salary.items():
            self.counter += 1
            print(f'{self.counter}. |{name}: {salary}\u00A3')
        self.total_number_of_employees()
        
name_salary = {}
while True:
    choice = input("\nTo exit, type ---Exit--- otherwise, press the Enter key: ")
    print('-'*70)
    if choice == 'Exit':
        break
    keys = input('\nName of the employee: ')
    values = input('Salary of the employee: ')
    name_salary[keys] = values
    
employees = Employee(0, name_salary) 
employees.info_about_employees()

print('#','-'*70)

classEmployee = {'The class inherited':Employee.__bases__, 'The class namespace ':Employee.__dict__,\
                 'the class name':Employee.__name__, 'The module name':Employee.__module__, \
                 'The documentation bar':Employee.__doc__}
x = 0
for key, value in classEmployee.items():
    x += 1
    print(f'\n{x}/{key}: {value}')


 
