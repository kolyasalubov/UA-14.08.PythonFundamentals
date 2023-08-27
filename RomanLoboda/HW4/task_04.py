input_temperature=int(input("Write a temperature in Celsius : "))

if input_temperature<-273.15:
    print(f"Enter the temperature in Celsius: {input_temperature} \
        \nError : Temperature is below absolute zero (-273.15°C)")
else :
    temperature_fahrenheit=int((input_temperature*9/5)+32)
    print(f"Enter the temperature in Celsius: {input_temperature} \
        \n{input_temperature}°C is equivalent to {temperature_fahrenheit}°F")