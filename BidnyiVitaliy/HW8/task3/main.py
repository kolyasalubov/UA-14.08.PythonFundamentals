from geometry import area_of

print('1 - area of rectangle')
print('2 - area of triangle')
print('3 - area of circle')
while True:
    o = input('Select option: ')
    if o == '1':
        a = float(input('Input width: '))
        b = float(input('Input length: '))
        print('area of rectangle is', area_of.rectangle(a, b))
    elif o == '2':
        a = float(input('Input side 1: '))
        b = float(input('Input side 2: '))
        c = float(input('Input side 3: '))
        print('area of triangle is', area_of.triangle(a, b, c))
    elif o == '3':
        r = float(input('Input radius: '))
        print('area of circle is', area_of.circle(r))
    else:
        break

