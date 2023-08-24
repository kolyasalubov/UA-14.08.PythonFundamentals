# TASK 1
line_16 = "Although never is often better than *right* now."
line_44 = "Readability counts."

# count
sentence1 = line_16.split()
sentence2 = line_44.split()

count_better = 0
count_never = 0
count_is = 0

for word in sentence1:
    if word == "better":
     count_better += 1
    if word == "never":
     count_never += 1
    if word == "is":
     count_is +=1

     print("-SENTENCE 1-")
     print("Count of 'better' for sentence 1:", count_better)
     print("Count of 'never' for sentence 1:", count_never)
     print("Count of 'is' for sentence 1:", count_is)

for word in sentence2:
    if word == "better":
     count_better += 1
    if word == "never":
     count_never += 1
    if word == "is":
     count_is +=1

print("\n-SENTENCE 2-")
print("Count of 'better' for sentence 2:", count_better)
print("Count of 'never' for sentence 2:", count_never)
print("Count of 'is' for sentence 2:", count_is)

# uppercase
uppercase_sentence1 = line_16.upper()
uppercase_sentence2 = line_44.upper()

print("\n-UPPERCASE-")
print("Uppercased sentence 1:", uppercase_sentence1)
print("Uppercased sentence 2:", uppercase_sentence2)

# replace
replace_sentence1 = line_16.replace("i", "&")
replace_sentence2 = line_44.replace("i", "&")

print("\n-REPLACE-")
print("Replace fot sentence 1:", replace_sentence1)
print("Replace fot sentence 2:", replace_sentence2)

# TASK 2
number = int(input("\nEnter four-digit natural number:"))
# product
k=1
for digit in str(number):
    k *= int(digit)

print ("Products of the digit: ", k)

# reverse
reversed_number = int(str(number)[::-1]) # [::-1] рядок навпаки
print("Reverse number:", reversed_number)

# ascending order
number = str(number)
number = ''.join(sorted(number))
number = int(number)
print("Sorted number:", number)

# TASK 3
a = 2
b = 7

a = a + b
b = a - b
a = a - b

print("\na:", a)
print("b:", b)