customer_number = int(input("Enter you number to calculate its factorial: "))
fact = 1
 
for i in range(1, customer_number + 1):
    fact = fact * i

if customer_number < 0:
    print("Factorial of negative numbers is not defined")
else:
    print(f"The factorial of {customer_number} is:",fact)











