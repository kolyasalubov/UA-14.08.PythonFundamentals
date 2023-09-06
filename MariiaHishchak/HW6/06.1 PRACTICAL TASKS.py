# Task 1
for i in (list(range(1, 11))):
     if i % 2 == 0:
         print(f"Number that are divisible by 2: {i}")
     if i % 3 == 0:
         print(f"Number that are divisible by 3: {i}")
     if i % 2 != 0 and i % 3 !=0:
         print (f"Number that are NOT divisible by 2 and 3: {i}")
# Task 2
login = str(input("Enter your login: "))
while login == "First":
    print("Congratulations!!!")
    break
else:
    print("ERROR")