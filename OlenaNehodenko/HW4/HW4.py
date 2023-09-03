#"Temperature Converter#
C=float(input("Enter the temperature in Celsius: "))
F=(C*9/5)+32
if C>=0:
   C=int(C)
   F=int(F)
   print(f"{C}°C is equivalent to {F}°F")
else:
   C=float(C)
   print(f"Temperature below absolute zero:({C}°C)")
