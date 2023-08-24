c_temperature = int(input('Enter the temperature in Celsius:'))

if c_temperature <= -273.15:
    print('Error: Temperature below absolute zero (-273.15°C)')
else:
    f_temperature = int((c_temperature*(9/5))+32)
    print(f'{c_temperature}°C is equivalent to {f_temperature}°F')
