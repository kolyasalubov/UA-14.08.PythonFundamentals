#First part in HW3 is to write Python's philosophy in the string format
#find The number of occurrences of the some words
my_string='''\nBeautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one and preferably only one obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea let's do more of those'''
print("The number of occurrences of the words 'better'=",my_string.find('better'))
print("The number of occurrences of the words 'never'=",my_string.find('never'))
print("The number of occurrences of the words 'is'=",my_string.find('is'))
#display all text in uppercase (all letters in uppercase)
print("Python's philosophy in uppercase:",my_string.upper())
#replace all occurrences of the symbol “i” with “&”
print("Python's philosophy with “&”:",my_string.replace('i','&'))

#Second part in HW3 is work with a four-digit natural number
#find the product of the digits of this number
N=int(input("Input a four-digit natural number:",))
prod=1
while N !=0:
    p=N%10
    prod=prod*p
    N=N//10
print(prod)

#write the number in reverse order
m = int(input("a four-digit natural number: "))
n = 0
while m > 0:
    digit = m % 10
    m = m // 10
    n = n * 10
    n = n + digit 
print('"Reverse" number:', n)

#sort the numbers included in the given number in ascending order
m = int(input("a four-digit natural number: "))
sorted_number = ''.join(sorted(str(m)))
print("The ascending sort version of number:", (sorted_number))

#Interchange the values ​of two variables without using the third variable
a=float(input("Enter fitrs variable:"))
b=float(input("Enter second variable:"))
a=a+b
b=a-b
a=a-b
print("Outputs two values:", (a),(b))