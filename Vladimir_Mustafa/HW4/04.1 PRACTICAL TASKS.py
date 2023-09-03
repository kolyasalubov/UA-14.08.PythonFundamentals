temperature_C = int(input('Enter temperature °C: '))
temperature_F = (temperature_C * 9 / 5) + 35

if -273.15 <= temperature_C <= 56.7:
    print(f'Temperature in Fahrenheit: {temperature_F}')

else:
    print('Error!!!')
