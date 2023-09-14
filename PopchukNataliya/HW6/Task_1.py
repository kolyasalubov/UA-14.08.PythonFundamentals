# In the range from1 to 10
# even numbers that are divisible by 2
even_2 =[x for x in range (10) if x % 2 == 0]
print(f"Even numbers in range (10) that sre divisible by 2: {even_2}")

# odd numbers, which are divisible by 3
odd_3 =[x for x in range (10) if x % 2 == 1 and x % 3 == 0]
print(f"Odd numbers, which are divisible by 3: {odd_3}")

# numbers that are not divisible by 2 and 3
num = [x for x in range(10) if not x % 2 == 0 if not x % 3 == 0]
print(f"Numbers that are not divisible by 2 and 3 : {num}")
