try:
    string_of_number = int(input("Please enter a four digit natural number: "))
except:
    print("You have entered not number.")
    exit(0)

sum_of_digits = 0
for i in string_of_number:
    sum_of_digits += int(i)

print(f"\nThe sum of these digits will be: {sum_of_digits}\n")

print(f"Number in revers order: {string_of_number[::-1]}", '\n')

print(f"Sorting in ascending order: {''.join(sorted(string_of_number))}", '\n')