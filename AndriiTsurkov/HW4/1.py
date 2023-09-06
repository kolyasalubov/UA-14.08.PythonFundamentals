user_celsius_temp = input("Enter temperature in Celsius: ")
try:
    user_celsius_temp_float = float(user_celsius_temp)
except:
    print("\nError: You entered the wrong value!")
    exit(0)

if user_celsius_temp_float < -273.15:
    print(f"Error this temperature below absolute zero (-273.15°C)"  )
    exit(0)
    
farengeyt_temp = (user_celsius_temp_float * (9/5)) + 32
print(f"{round(user_celsius_temp_float)}°C is equivalent to {round(farengeyt_temp)}°F")

