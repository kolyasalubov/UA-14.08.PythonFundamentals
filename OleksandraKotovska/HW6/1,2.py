############ First task ##############

even = []
odd3 = []
other_odd = []

for i in range(1, 10):
    if i % 2 == 0:
        even.append(i)
    elif i % 3 == 0:
        odd3.append(i)
    elif i % 2 != 0 and i % 3 != 0:
        other_odd.append(i)

text = "In range from 1 to 10 there are"
print(text,"even numbers:\n",even)
print(text,"odd numbers, which are divisible by 3:\n",odd3)
print(text,"numbers that are not divisible by 2 and 3:\n",other_odd)


########## Second task ##################


user_login = input("Enter your login: ")

while user_login == "First":
    print("Congratulations!")
    break
else:
    print("Your login is incorrect!")

