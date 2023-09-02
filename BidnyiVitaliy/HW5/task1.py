#Create a list that contains elements of integer type, then
#use the loop to change the type of these elements to a floating
#type.
#(Hint: use the built-in float () function).

a=[2,9,2,0,2,3]
print(a)
for i in range(len(a)):
  a[i] = float(a[i])
print(a)