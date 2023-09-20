import calculate_area

while True:
    print("Вибери фігуру, площу якої ми будемо вичислювати:\n1)Прямокутник  \n2)Трикутник  \n3)Коло")

    choice = input("Вибери цифру, дану для фігури: ")

    if choice == '1':
        a = float(input("Введи довжину прямокутника (a): "))
        b = float(input("Введи ширину прямокутника (b): "))
        result = calculate_area.rectangle_area(a, b)
        print(f"Площа прямокутника = {result}")
        break
    elif choice == '2':
        h = float(input("Введіть висоту трикутника (h): "))
        a = float(input("Введіть довжину сторони (a): "))
        result = calculate_area.triangle_area(h, a)
        print(f"Площа прямокутника = {result}")
        break
    elif choice == '3':
        r = float(input("Введіть радіус кола (r): "))
        result = calculate_area.circle_area(r)
        print(f"Площа кола = {result}")
        break
    else:
        print("Такого варіанту немає! Будь ласка оберіть один з цих варіантів: \n1)Прямокутник  \n2)Трикутник  \n3)Коло")
        choice = input("Вибери цифру, дану для фігури: ")