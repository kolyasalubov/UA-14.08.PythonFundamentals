# # task1
# divisible_by_two = []
# divisible_by_three = []
# not_divisible_by_two_and_three = []
# for i in range(1,11):
#     if i % 2 == 0:
#         divisible_by_two.append(i)
#     if i % 2 == 1 and i % 3 == 0:
#         divisible_by_three.append(i)
#     if i % 2 != 0 and i % 3 != 0:
#         not_divisible_by_two_and_three.append(i)
#
# print("Even numbers that are divisible by 2: ",divisible_by_two)
# print("Odd numbers that are divisible by 3: ", divisible_by_three)
# print("Numbers that aren't divisible by 2 and 3: ", not_divisible_by_two_and_three)
#
# #task2
# correct_login = "First"
# while True:
#     user_login = input("Enter ur login: ")
#     if user_login == correct_login:
#         print("Welcome!")
#         break
#     else:
#         print("Incorrect login! Please try again <3")