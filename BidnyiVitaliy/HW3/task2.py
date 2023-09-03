# 2. A four-digit natural number is specified:
# - find the product of the digits of this number
# - write the number in reverse order
# - in ascending order, you need to sort the numbers included in the given number
#Задано чотиризначне натуральне число:
# - знайти добуток цифр цього числа
# - запишіть число у зворотному порядку
# - у порядку зростання потрібно відсортувати числа, що входять до заданого числа1983

number = input("Введіть чотиризначне натуральне число:")

result1 =int(number[0])*int(number[1])*int(number[2])*int(number[3])
result2 = number[::-1]
list_number = list(number)
list_number.sort()
result3 = list_number

print("добуток цифр дорівнює:", result1)
print("число у зворотному порядку:", result2)
print("відсортовані цифри у порядку зростання:", result3)