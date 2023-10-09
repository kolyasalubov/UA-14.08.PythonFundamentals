for num in range (1,11):
    if num % 2 == 0 and num % 3 == 0:
        print(f"number divisible by 2 and 3:({num})") 
    elif num % 3 == 0:
        print(f"odd number divisible by 3:({num})")
    elif num % 2 == 0:
        print(f"even number divisible by 2:({num})")
    else:
        print(f"not divisible number by 2 and 3:({num})")