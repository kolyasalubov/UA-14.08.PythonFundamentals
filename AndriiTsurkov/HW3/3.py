first_variable = "Hello"
second_variable = 2023

print("\nBefore change:")
print(f"First variable  = {first_variable}")
print(f"Second variable = {second_variable}")

first_variable, second_variable = second_variable, first_variable

print("\nAfter change:")
print(f"First variable  = {first_variable}")
print(f"Second variable = {second_variable}")