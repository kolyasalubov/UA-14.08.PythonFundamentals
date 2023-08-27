c = float(input("Enter temperature in Celsius: \n"))
f = float((c*9/5)+32)
if c<=-273.15:
    print("Error! Impossible temperature")
else:
    print(f)