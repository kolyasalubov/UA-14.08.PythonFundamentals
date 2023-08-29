temperature_in_celsius = float(input("Enter temperature in Celsius: "))
if temperature_in_celsius < -273.15:
    print("ERROR!!! \n Temperature can't be lower!")
else:
  temperature_in_fahrenheit = (temperature_in_celsius * 9/5) + 32
  print("Temperature in Fahrenheit: ", temperature_in_fahrenheit, "F")
