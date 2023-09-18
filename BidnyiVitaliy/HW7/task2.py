# Write a program that calculates the area of a rectangle,
# triangle and circle
# (write three functions to calculate the area, and call them in the
# main program depending on the user's choice).

# Напишите программу, вычисляющую площадь прямоугольника.
# треугольник и круг
# (напишите три функции для вычисления площади и вызовите их в
# основная программа в зависимости от выбора пользователя).
import math

def rectangle(a, b):
    return a * b

def triangle(a, b, c):
    p = (a + b + c)/2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s

def circle(r):
    return  math.pi * r * r

print('1 - area of rectangle')
print('2 - area of triangle')
print('3 - area of circle')
while True:
    o = input('Select option: ')
    if o == '1':
        a = float(input('Input width: '))
        b = float(input('Input length: '))
        print('area of rectangle is', rectangle(a, b))
    elif o == '2':
        a = float(input('Input side 1: '))
        b = float(input('Input side 2: '))
        c = float(input('Input side 3: '))
        print('area of triangle is', triangle(a, b, c))
    elif o == '3':
        r = float(input('Input radius: '))
        print('area of circle is', circle(r))
    else:
        break











