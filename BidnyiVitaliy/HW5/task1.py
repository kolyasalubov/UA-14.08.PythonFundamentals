for n in range(1, 10):
    if n % 2 == 0:
        print('{} is even number'.format(n))
    if    (n%2 == 1) and(n%3 == 0):
        print('{} is odd number, which is divisible by 3'.format(n))
    if    (n%2 != 0) and(n%3 != 0):
        print('{} is not divisible by 2 and 3'.format(n))

#Create a list that contains elements of integer type, then
#use the loop to change the type of these elements to a floating
#type.
#(Hint: use the built-in float () function).

a=[2,9,2,0,2,3]
print(a)
for i in range(len(a)):
  a[i] = float(a[i])
print(a)

