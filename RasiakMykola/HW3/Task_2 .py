
# 03.1 PRACTICAL TASKS / [GITHUB]


# Task 2
four_digit_natural_number = "6274"

a, b, c, d = four_digit_natural_number[0], four_digit_natural_number[1], \
             four_digit_natural_number[2], four_digit_natural_number[3]

the_product_of_the_digits = int(a)*int(b)*int(c)*int(d)

reverse_order = int(four_digit_natural_number[-1] + four_digit_natural_number[-2] + \
                four_digit_natural_number[-3] + four_digit_natural_number[-4])

                   
sort_the_numbers = "{b}{d}{a}{c}" .format (a = four_digit_natural_number[0], b = four_digit_natural_number[1], \
                                              c = four_digit_natural_number[2], d = four_digit_natural_number[3])                

print(f"\nThe product of a number {four_digit_natural_number } is equal to {the_product_of_the_digits}")
print(f"\nThe four-digit natural number {four_digit_natural_number} in reverse order {reverse_order}")
print(f"\nThe number 6274 in sorted order is {sort_the_numbers}.")

