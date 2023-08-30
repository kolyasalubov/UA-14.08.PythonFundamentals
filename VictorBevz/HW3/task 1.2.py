num = 1234 
num1 = list(str(num))
list = list(num1)
list.reverse()
num2 = "".join(list)
print('Reversed:', num2) 

num1.sort()
print(num1)

a=int(num1[0])
b=int(num1[1])
c=int(num1[2])
d=int(num1[3])
print("Product =", a*b*c*d)