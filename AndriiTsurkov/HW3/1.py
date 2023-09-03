python_philosophy_str = "If the implementation is hard to explain, it's a bad idea."

ocurency_better = 0
ocurency_never  = 0 
ocurency_is     = 0

#python_philosophy_list = python_philosophy_str.split()

for word in python_philosophy_str.lower().replace('.', '').replace(',', '').split():

    if word == "better":
        ocurency_better += 1
    elif word == "never":
        ocurency_never += 1
    elif word == "is":
        ocurency_is += 1
    
print(f"In phrase: {python_philosophy_str}")
print(f"We have find: \n'better' - {ocurency_better}")
print(f"'never' - {ocurency_never}")
print(f"'is' - {ocurency_is}")

print(f"\nLine in Uppercase: {python_philosophy_str.upper()}")

print(f"\nReplace all symbols 'i' on '&': {python_philosophy_str.replace('i', '&')}")
