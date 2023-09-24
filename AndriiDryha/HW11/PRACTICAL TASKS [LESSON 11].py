# # Task 1

# def number_type():
#     try:
#         age = int(input('Enter your age:\n'))
#         try:
#             if age > 0 and age % 2 == 0:
#                 print(f"Age {age} is even.")
#             elif age > 0 and  age % 2 != 0:
#                 print(f"Age {age} is odd.")
#             elif age <= 0:
#                 raise ValueError()  
#         except ValueError:
#             print("Age should be above 0")  
#             number_type()     
#     except:
#         print('Incorrect input.')
#         number_type()
       
# number_type()

# Task 2

def day_number():
    try:
        number = int(input('Enter the number of the day:\n'))
        try:
            if number == 1:
                print(f"{number} is Monday.")
            elif number == 2:
                print(f"{number} is Tuesday.")
            elif number == 3:
                print(f"{number} is Wednesday.")  
            elif number == 4:
                print(f"{number} is Thursday.") 
            elif number == 5:
                print(f"{number} is Friday.") 
            elif number == 6:
                print(f"{number} is Saturday.") 
            elif number == 7:
                print(f"{number} is Sunday.") 
            elif number <= 0 or number > 7:
                raise ValueError()  
        except ValueError:
            print("Number should be ranging between 1 and 7.")  
            day_number()     
    except:
        print('Incorrect input.')
        day_number()
       
day_number()

