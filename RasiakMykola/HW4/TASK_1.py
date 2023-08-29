
# 04.1 PRACTICAL TASKS / [GITHUB]


# Task1. "Temperature Converter"
celsius = float(input("\nEnter the temperature in Celsius: "))
                
if celsius < -273.15 :
    
    print("\nError: Temperature below absolute zero (-273.15°C)")

else :
    
    F = (celsius*9/5)+32
    print(f"\n{celsius}°C is equivalent to {F}°F")
