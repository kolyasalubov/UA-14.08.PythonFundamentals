from math import sqrt, pi


def rectangle_area(height: float, width: float) -> float:
    """

    :param height: height of the rectangle
    :param width: width of the rectangle

    :return: return the area of the rectangle
    """

    return height * width


def triangle_area(a: float, b: float, c: float) -> float:
    """
    This funcoin uses Heron's formula

    :param a: side AB of the triangle
    :param b: side BC of the triangle
    :param c: side CD of the triangle

    :return: return the area of the triangle
    """
    try:
        p = (a + b + c) / 2  # half perimetr

        area = sqrt(p * (p - a) * (p - b) * (p - c))
        area = round(area, 2)

        return area
    except ValueError:
        print('\nImpossible triangle!!!')


def circle_area(rad: float) -> float:
    """

    :param rad: radius of the circle

    :return: return the area of the triangle
    """

    PI = round(pi, 2)
    s = PI * (rad ** 2)
    return s


def choice():
    while True:
        print('Which figure area you want to calculate?\n'
              '1: Rectangle\n'
              '2: Triangle\n'
              '3: Circle\n'
              '0: Exit\n')

        choice = input('>>> ')

        if choice == '1':
            h = float(input('Enter height of rectangle: '))
            w = float(input('Enter wight of rectangle: '))
            print('Area = ', rectangle_area(h, w), '\n')

        elif choice == '2':
            a = float(input('Enter side AB: '))
            b = float(input('Enter side BC: '))
            c = float(input('Enter side CD: '))
            print('Area = ', triangle_area(a, b, c), '\n')

        elif choice == '3':
            r = float(input('Enter radius of circle: '))
            print('Area = ', circle_area(r), '\n')

        elif choice == '0':
            print('Goodbye!')
            break


choice()
