numb =2456 #наше відоме число
numb1 = list(str(numb))
n_list = list(numb1)
n_list.reverse()
n2 = "".join(n_list)
print('"Revers number is:', n2) #in rewers mode

# product of nubers
a=int(numb1[0])
b=int(numb1[1])
c=int(numb1[2])
d=int(numb1[3])
print("Product of Numbers = ", a*b*c*d)

#sort
numb1.sort()
print(numb1)

