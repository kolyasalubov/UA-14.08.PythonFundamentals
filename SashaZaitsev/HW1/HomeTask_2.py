#Привіт! Ця программа вираховує суму, різницю, добуток і т.д. з двух чисел
#Тут я вирішив трішки замудрити, але надіюсь, що це тільки на краще!
import time
print("Привіт, це невеличкий калькулятор, що допоможе тобі вирахувати суму двох чисел")
while True:
    try:
        a = float(input('Введіть пeрше число: '))
        print(a)
        break
    except ValueError:
        print("Вводити можна лише число!")
while True:
    try:
        b = float(input('Введіть друге число: '))
        print(b)
        break
    except ValueError:
        print("Вводити можна лише число!")
operation = input("Яку математичну дію ми проводимо * - + ** / // %: ")
print("Зачекайте, ми оброблюємо ваш запит...")
time.sleep(3)
result = 0
while True:
    if operation == '*':
        result = a * b
        break
    elif operation == '-':
        result = a - b
        break
    elif operation == '+':
        result = a + b
        break
    elif operation == '**':
        result =  a ** b
        break
    elif operation == '/':
        result = a / b
        break
    elif operation == '//':
        result = a // b
        break
    elif operation == '%':
        result = a % b
        break
    else:
        print("Вмбачте, але такого я не вмію, оберіть інший варіант!")
        operation = input("Яку математичну дію ми проводимо * - + ** / // %: ")
print(f"Ось ваш результат: {result}")
print('Дякую за увагу!')