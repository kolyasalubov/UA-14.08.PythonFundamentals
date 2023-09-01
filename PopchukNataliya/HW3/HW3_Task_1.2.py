# 1.1 The product of the digits (first solution)
number = input("Enter a four digital number:")
product = (int(number) % 10) * (int(number) // 10 % 10) * (int(number) // 100 % 10) * (int(number) // 1000)
print(product)

# 1.2 The product of the digits (second solution)
number = input("Enter a four digital number:")
product = 1
for char in number:
    digit = int(char)
    product *= digit

print("product of digits=", product)


# 2.1 Write the number in reverse order (first solution)
print(input("Enter a four digital number:")[::-1])

# 2.2 Write the number in reverse order (second solution)
number = input("Enter a four digital number:")
print(int(number) % 10)
print(int(number) // 10 % 10)
print(int(number) // 100 % 10)
print(int(number) // 1000)

# 3.1 Sort numbers in ascending order
number = input("Enter a four digital number:")
digits =[int(d) for d in str(number)]
sorted_digits= sorted(digits)
print(sorted_digits)
