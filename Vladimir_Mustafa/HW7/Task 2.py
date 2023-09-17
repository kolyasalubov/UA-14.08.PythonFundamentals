what_area = print('What area do you want to find?')
enter_area = int(input('Enter 1 - сircle, 2 - rectangle or 3 - triangle: '))


def сircle():
    p = float(input('Enter π:'))
    r = float(input('Enter R:'))
    s = p * r ** 2
    print(f'S = {s}')


def rectangle():
    a = float(input('Enter side a:'))
    b = float(input('Enter side b:'))
    s = a * b
    print(f'S = {s}')


def triangle():
    a = float(input('Enter side a:'))
    b = float(input('Enter side b:'))
    c = float(input('Enter side c:'))
    s = (a + b + c) / 2
    print(f'S = {s}')


if enter_area == 1:
    сircle()
elif enter_area == 2:
    rectangle()
elif enter_area == 3:
    triangle()
else:
    print('ERROR!!!')


























