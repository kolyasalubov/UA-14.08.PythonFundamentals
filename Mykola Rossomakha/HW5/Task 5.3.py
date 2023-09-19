n = int(input("Enter a number for factorial calculation: "))
f = 1

for i in range(1, n + 1):
    f = f * i

if n < 0:
    print("Factorial for negative numbers is undefined.")
else:
    print(f"Factorial of {n} is:", f)