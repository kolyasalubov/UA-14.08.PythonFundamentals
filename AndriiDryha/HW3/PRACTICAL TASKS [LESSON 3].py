# Task 1

Text = """1.Beautiful is better than ugly.
2.Explicit is better than implicit.
3.Simple is better than complex.
4.Complex is better than complicated.
5.Flat is better than nested.
6.Sparse is better than dense.
7.Readability counts.
8.Special cases aren't special enough to break the rules.
9.Although practicality beats purity.
10.Errors should never pass silently.
11.Unless explicitly silenced.
12.In the face of ambiguity, refuse the temptation to guess.
13.There should be one-- and preferably only one --obvious way to do it.
14.Although that way may not be obvious at first unless you're Dutch.
15.Now is better than never.
16.Although never is often better than *right* now.
17.If the implementation is hard to explain, it's a bad idea.
18.If the implementation is easy to explain, it may be a good idea.
19.Namespaces are one honking great idea -- let's do more of those!
20.Beautiful is better than ugly.
21.Explicit is better than implicit.
22.Simple is better than complex.
23.Complex is better than complicated.
24.Flat is better than nested.
25.Sparse is better than dense.
26.Readability counts.
27.Special cases aren't special enough to break the rules.
28.Although practicality beats purity.
29.Errors should never pass silently.
30.Unless explicitly silenced.
31.In the face of ambiguity, refuse the temptation to guess.
32.There should be one-- and preferably only one --obvious way to do it.
33.Although that way may not be obvious at first unless you're Dutch.
34.Now is better than never.
35.Although never is often better than *right* now.
36.If the implementation is hard to explain, it's a bad idea.
37.If the implementation is easy to explain, it may be a good idea.
38.Namespaces are one honking great idea -- let's do more of those!Beautiful is better than ugly.
39.Explicit is better than implicit.
40.Simple is better than complex.
41.Complex is better than complicated.
42.Flat is better than nested.
43.Sparse is better than dense.
44.Readability counts.
45.Special cases aren't special enough to break the rules.
46.Although practicality beats purity.
47.Errors should never pass silently.
48.Unless explicitly silenced.
49.In the face of ambiguity, refuse the temptation to guess.
50.There should be one-- and preferably only one --obvious way to do it.
51.Although that way may not be obvious at first unless you're Dutch.
52.Now is better than never.
53.Although never is often better than *right* now.
54.If the implementation is hard to explain, it's a bad idea.
55.If the implementation is easy to explain, it may be a good idea.
56.Namespaces are one honking great idea -- let's do more of those!"""
start = -1
count1 = 0
count2 = 0
count3 = 0

while True:
    start = Text.find("better", start+1)
    if start == -1:
        break
    count1 += 1

print("The number of words 'better' in the current text is ", count1)

while True:
    start = Text.find("never", start+1)
    if start == -1:
        break
    count2 += 1

print("The number of words 'never' in the current text is ", count2)

while True:
    start = Text.find("is", start+1)
    if start == -1:
        break
    count3 += 1

print("The number of words 'is' in the current text is ", count3)

Text = Text.upper()
Text = Text.replace('I', '&')

print("Uppercase text with replace of letters 'i' on '&': \n", Text, sep = '')


# # Task 2

# while True:
#     try:
#         number = int(input("Enter the four-digit natural number \n"))
#         assert 999 < number < 10000
#     except ValueError:
#         print("Not an integer! Please enter an integer.")
#     except AssertionError:
#         print("Please enter an integer between 1000 and 9999")
#     else:
#         n = number
#         mult = 1
#         if n == 0:
#             mult = 0
#     while (n != 0):
#         mult = mult * (n % 10)
#         n = n // 10

#     print("Product of the digits of the number", mult)

#     #Reversed number

#     def reversed1(variable):
#         res=''.join(reversed(variable))
#         return res
    
#     m = reversed1(str(number))

    
#     print("Reversed number", m)

#     #Ascending order

#     a = str(number)
#     b = list(a)
#     l = sorted(b)
#     result = int(''.join(map(str, l)))
    

#     print("Ascending order ", result)



# # Task 3

# x = input("Enter number x \n")
# y = input("Enter number y \n")

# x = int(x)**int(y)
# y = int(x)//int(y)

# print("After interchange x =", x, ", y =", y)