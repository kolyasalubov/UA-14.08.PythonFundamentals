input_string=input("Write the line from 'The Zen of Python' file : ").lower()

better_counter=0
never_counter=0
is_counter=0

words=input_string.split()

for word in words:
    if "better" == word:
        better_counter+=1
    elif "never" == word:
        never_counter+=1
    elif "is" == word:
        is_counter+=1

upper_input_string=input_string.upper()
replaced_text=input_string.replace("i", "&")



print(f"\nThe number of occurrences of the word 'better' is {better_counter}")
print(f"The number of occurrences of the word 'never' is {never_counter}")
print(f"The number of occurrences of the word 'is' is {is_counter}")

print(f"All letter in uppercase : {upper_input_string}")
print(f"The text where 'i' was replaced by '&' : {replaced_text}")


