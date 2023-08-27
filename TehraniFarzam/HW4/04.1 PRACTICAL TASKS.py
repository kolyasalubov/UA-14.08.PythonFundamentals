celsius = input("Enter temperature in Celsius: ")

if celsius.replace('.', '', 1).isdigit() or \
        (celsius.startswith('-') and celsius[1:].replace('.', '', 1).isdigit()):

    celsius = float(celsius)
    if celsius < -273.15:
        print("Temperature below absolute zero(-273.15^c)")
    else:
        fahrenheit = (celsius * 9/5) + 32
        print(fahrenheit)
else:
    print("Invalid input.")