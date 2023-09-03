# Example output:
# Enter the temperature in Celsius: 25
# 25°C is equivalent to 77°F
# Example output (if the user enters a temperature below absolute zero):
# Enter the temperature in Celsius: -300
# Error: Temperature below absolute zero (-273.15°C)

c = float (input ('Enter the temperature in Celsius:') )

if c < -273.15:
    print('Error: Temperature below absolute zero (-273.15°C)')
else:
    f = c * 9/5 + 32
    print('{}°C is equivalent to {}°F'.format(c, f))