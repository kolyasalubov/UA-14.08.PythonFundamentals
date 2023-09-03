# Temperature converter
t = float(input('Enter the temperature in Celsius:'))
if t > -273.15:
    t_K = (t * 9 / 5) + 32
    print(f"{t}°C is equivalent to {t_K}°F")
else:
    print("Error:Temperature below absolute zero -273.15")

