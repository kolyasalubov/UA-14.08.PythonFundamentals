#Temperature converter

temperature_celsius = int(input("Enter the temperature in Celsius: \n"))

temperature_fahrenheit = (temperature_celsius * 9/5) + 32

if temperature_celsius > -273.15:
    print(f"{temperature_celsius}°C is equal to {temperature_fahrenheit}°F")
else:
    print("Temperature below absolute zero (-273.15°C)")