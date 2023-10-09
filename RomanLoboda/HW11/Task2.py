import logging

days = ["monday", "thursday", "wednesday", "tuesday", "friday", "saturday", "sunday"]
logging.basicConfig(format='%(process)d-%(levelname)s-%(asctime)s-%(message)s', level=logging.INFO)


def input_value():
    input_value = int(input("Enter number : "))
    if input_value>0:
        print(f"{input_value} is {days[input_value - 1]}")
    else:
        print("Enter positive number")


try:
    input_value()
except IndexError as e:
    logging.warning(e)
except ValueError as b:
    logging.warning(b)
