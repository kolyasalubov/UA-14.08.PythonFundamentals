a = input("Please enter the first number:\t")
b = input("Please enter the sekond number:\t")

try:
    a = int(a)
    b = int(b)
except:
    print("\nYou have enter not digits!\nPlese try one more time.\n")
    exit()

print()
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a ** b = {a ** b}")
print(f"a // b = {a // b}")
print(f"a % b = {a % b}")
print()