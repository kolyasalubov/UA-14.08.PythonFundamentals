#3. Interchange the values of two variables without using the third variable.
a = int(input("a: "))
b = int(input("b: "))

a=a+b
b=a-b
a=a-b

print('a =', a)
print('b =', b)