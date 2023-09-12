import area_modul

print("Here you can calculate the area of a rectangle, triangle and circle")
user_choice = input("Choose figure you want to calculate the area: ")
wrong_data = "Wrong data, enter an integer"
if user_choice == "rectangle":
    r1 = (input("Enter the first side: "))
    r2 = (input("Enter the second side: "))
    if not r1.isdigit() or not r2.isdigit():
        print(wrong_data)
    else:
        print("The area is:",area_modul.rectangle_area(int(r1), int(r2)))
elif user_choice == "triangle":
    b = input("Enter the base: ")
    h = input("Enter the hight: ")
    if not b.isdigit() or not h.isdigit():
        print(wrong_data)
    else:
        print("The area is:",(area_modul.triangle_area(int(b), int(h))))

elif user_choice == "circle":
    r = input("Enter the radius: ")
    if not r.isdigit():
        print(wrong_data)
    else:
        print("The area is:",(area_modul.circle_area(int(r))))
else:
    print("Enter rectangle, triangle or circle")
