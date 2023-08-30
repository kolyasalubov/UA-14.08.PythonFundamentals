temp_C = int(input("Enter a temperature in Celsius:"))
temp_F = temp_C * 9/5 + 32
if temp_C < -273.15:
    print("Error: The temperature is below absolute zero(273.15)")
else: 
    print(f"{temp_C} degrees in Celsius is equal to {temp_F} degrees in Farenheit")