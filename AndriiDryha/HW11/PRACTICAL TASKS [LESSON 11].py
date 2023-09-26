# # Task 1 v1.0

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

# # Task 1 v2.0

# def number_type():
#     try:
#         age = int(input('Enter your age:\n'))
#         if age > 0:
#             if age % 2 == 0:
#                 print(f"Age {age} is even.")
#             else:
#                 print(f"Age {age} is odd.")
#         else:
#             print("Age should be above 0")
#         number_type()
#     except ValueError:
#         print("Invalid input. Age should be a positive integer.")
#         number_type()
#     except KeyboardInterrupt:
#         print("\nExiting...")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         number_type()

# number_type()

# # Task 2 v1.0

# def day_number():
#     try:
#         number = int(input('Enter the number of the day:\n'))
#         try:
#             if number == 1:
#                 print(f"{number} is Monday.")
#             elif number == 2:
#                 print(f"{number} is Tuesday.")
#             elif number == 3:
#                 print(f"{number} is Wednesday.")  
#             elif number == 4:
#                 print(f"{number} is Thursday.") 
#             elif number == 5:
#                 print(f"{number} is Friday.") 
#             elif number == 6:
#                 print(f"{number} is Saturday.") 
#             elif number == 7:
#                 print(f"{number} is Sunday.") 
#             elif number <= 0 or number > 7:
#                 raise ValueError()  
#         except ValueError:
#             print("Number should be ranging between 1 and 7.")  
#             day_number()     
#     except:
#         print('Incorrect input.')
#         day_number()
       
# day_number()

# Task 2 v2.0

def day_number():
    try:
        number = int(input('Enter the number of the day:\n'))
        if 1 <= number <= 7:
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            print(f"{number} is {days[number - 1]}.")
        else:
            print("Number should be ranging between 1 and 7.")
        day_number()
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 7.")
        day_number()
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"An error occurred: {e}")
        day_number()

day_number()



