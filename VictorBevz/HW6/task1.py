list1 = []
list2 = []
list3 = []

for i in range(1, 10):
    if i%2 == 0:
        list1.append(i)
    elif i%3 == 0:
        list2.append(i)
    else:
        list3.append(i)

print(list1, list2, list3)