#Temperature converter

C = int(input("Enter the temperature in Celsius: \n"))

F = (int(C)*9/5)+32

print(C, "°C is equal to ", F, "°F ", sep = '') if C > -273.15 else print("Temperature below absolute zero (-273.15°C)")
