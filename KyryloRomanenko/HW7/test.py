height = input("Enter height:")

while True:
    try:
        height = float(height)
        break
    except ValueError:
        print("Invalid input. Please enter a float.")
        height = input("Enter height:")