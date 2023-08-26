#temperature conventer
celsius_temp = float(input('Enter the temperature in celsius : '))
if celsius_temp >= -273.15:
    print(celsius_temp,'C is equivalent', celsius_temp*9/5+32,'F')
else:
    print('ERROR!The temperature is below absolut zero(-273.15C)')