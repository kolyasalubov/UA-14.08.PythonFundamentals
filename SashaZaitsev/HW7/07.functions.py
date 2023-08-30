# Functions
def large_num(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        print("Числа рівні")
        return x, y

print(large_num(5, 5))

def area_circle():
    print("Вираховуємо площу кола")
    while True:
        try:
            radius = float(input('Введіть радіус: '))
            break
        except ValueError:
            print("Вводити можна лише число!")
    radius_1 = radius * radius 
    operation = 3.14 * radius_1
    print("Площа кола:", operation)
area_circle()

def area_rectangle():
    print("Вираховуємо площу прямокутника")
    while True:
        try:
            width = float(input('Введіть ширину: '))
            length = float(input('Введіть довжину: '))
            break
        except ValueError:
            print("Вводити можна лише число!")
    operation = width * length
    print("Площа прямокутника:", operation)
area_rectangle()
    
def area_triangle():
    print("Вираховуємо площу трикутника")
    while True:
        try:
            side_a = float(input('Введіть катет а: '))
            side_b = float(input('Введіть катет b: '))
            break
        except ValueError:
            print("Вводити можна лише число!")
    operation = 1/2 * side_a * side_b
    print("Площа трикутника:", operation)
area_triangle()

from collections import Counter

S ='hello'
S = S.lower()
d = Counter(S)
for item, ct in d.items():
    print('%s : %d' % (item, ct))