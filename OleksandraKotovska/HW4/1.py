temperature_celsius = float(input("Enter the temperature in Celsius: "))
Fahrenheit = (temperature_celsius * 9/5) + 32

if temperature_celsius >= -273.15 and temperature_celsius <= 1000000:
	print(temperature_celsius,"\U000000B0C is equivalent to", Fahrenheit,"\U000000B0F")
elif temperature_celsius < -273.15:
	print("Error: Temperature below absolute zero (-273.15\U000000B0C)")
else:
	print("Error: Temperature above 1000000\U000000B0C")

