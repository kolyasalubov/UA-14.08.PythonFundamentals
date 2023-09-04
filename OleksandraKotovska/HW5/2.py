number_1 = 0
number_2 = 1
count = 0
stop_number = int(input("Enter your number to stop fibonacci sequence: "))

while count < stop_number:
    print(number_1)
    number_3 = number_1 + number_2
    number_1 = number_2
    number_2 = number_3
    count += 1
    if number_1 >= stop_number:
       break
    







        




















