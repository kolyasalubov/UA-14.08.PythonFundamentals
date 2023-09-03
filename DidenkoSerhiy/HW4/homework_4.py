c = float(input("Input the temperature in Celcius: "))
          
f = c * 9/5 + 32

if c > -273.1:
    print(c,'\u00b0C' ' is equivalent', f,'\u00b0F')
elif c <= -273.15:
    print("Error: Temperature below absolute zero -273.15\u00b0С")