input_number=input("Write four-digit natural number : ")


digits_product=1
for number in input_number:
    digits_product*=int(number)

revers_number=input_number[::-1]
sorted_nuber="".join(sorted(input_number))


print(f"\nThe product of the digits {input_number} is {digits_product}")
print(f"The number in reverse order is {revers_number}")
print(f"The sorted number is {sorted_nuber}")


