# Сollections
for i in range(1, 10):

    if i % 2 == 0:
        print(i, end = ' ')
        print("Числа парні")
    elif i % 2 != 0 and i % 3 == 0:
        print(i, end = ' ')
        print("Непарні, що діляться на три")
    else:
        print(i, end = ' ')
        print("Числа, що не діляться на три та два")
        
while True:
    login = input("Введіть свій логін: ")
    if login == "First":
        print("Чудово! Вірний логін!")
        break
    else:
        print("Неправильний логін!")
