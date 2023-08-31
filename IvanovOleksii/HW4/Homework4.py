while True:
    enter_celsius = float(input('Enter a temperature in Celsius: '))
    if enter_celsius < -273.15:
        print('Error: Temperature below absolute zero(-273.15°C)\n'
              'Try again')
    else:
        fareheit = (enter_celsius * 9 / 5) + 32
        print(f'{enter_celsius}°C is equivalent to {fareheit}°F')
        break

