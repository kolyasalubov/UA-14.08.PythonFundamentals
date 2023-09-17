import sys

celsius = float(input("Enter temperature in Celsius:"))
if celsius > float(273.15):
    print("Your temperature is not in the range of absolute zero")
    sys.exit()
else:
    print("Invalid temperature")

fahrenheit = (celsius * 9 / 5) + 32
print(f"Celsius{celsius} in Fahrenheit = {fahrenheit}")
