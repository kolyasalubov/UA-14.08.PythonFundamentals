# #task1
# def age_entering():
#     while True:
#         try:
#             age = int(input("Enter your age: "))
#             if age < 0:
#                 raise ValueError("Age can't be negative.")
#             else:
#                 if age % 2 == 0:
#                     print("Your age is even.")
#                 else:
#                     print("Your age is odd.")
#         except ValueError as e:
#             print(e)
#
# age_entering()

# #task2
# def day_of_week():
#     while True:
#         try:
#             day_number = int(input("Enter a number between 1 and 7 to get the proper day of the week\n"))
#             if day_number >= 1 and day_number <= 7:
#                 days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#                 day = days[day_number -1]
#                 print(f"Your day is {day}")
#             else:
#                 print("Enter number between 1 and 7")
#         except ValueError:
#             print("Invalid input! Please enter a number.")
#
#
# day_of_week()

