from area_calc import *

input_area = input("What area need to be calculate ? (rectangle, triangle, circle) : ")

if input_area == "rectangle":
    w = int(input("Enter width : "))
    h = int(input("Enter height : "))
    print("The area of rectangle : ", area_rectangle(w, h))
elif input_area == "triangle":
    b = int(input("Enter base : "))
    h = int(input("Enter height : "))
    print("The area of triangle : ", round(area_triangle(b, h), 2))
elif input_area == "circle":
    r = int(input("Enter radius : "))
    print("The area of circle : ", round(area_circle(r), 2))
else:
    print("Error, incorrect value ")