import time

print('"Zen of Python')
time.sleep(3)

s = "1.Beautiful is better than ugly, \n"\
    "2.Explicit is better than implicit,\n"\
    "3.Simple is better than complex, \n"\
    "4.Complex is better than complicated, \n"\
    "5.Flat is better than nested, \n"\
    "6.Sparse is better than dense,\n"\
    "7.Readability counts.\n"\
    "8.Special cases aren't special enough to break the rules.\n"\
    "9.Although practicality beats purity.\n"\
    "10.Errors should never pass silently.\n"\
    "11.Unless explicitly silenced.\n"\
    "12.In the face of ambiguity, refuse the temptation to guess.\n"\
    "13.There should be one-- and preferably only one --obvious way to do it.\n"\
    "14.Although that way may not be obvious at first unless you're Dutch.\n"\
    "15.Now is better than never.\n"\
    "16.Although never is often better than *right* now.\n"\
    "17.If the implementation is hard to explain, it's a bad idea.\n"\
    "18.If the implementation is easy to explain, it may be a good idea.\n"\
    "19.Namespaces are one honking great idea -- let's do more of those!\n"\
    
print(s.upper())

time.sleep(5)
print("Let's count how many times the word \"better\" occur in \"Zen of Python\":\
    it's", s.count("better"))
time.sleep(5)

print("Let's count how many times the word \"never\" occur in \"Zen of Python\":\
    it's", s.count("never"))
time.sleep(5)

print("Let's count how many times the word \"is\" occur in \"Zen of Python\":\
    it's", s.count("is"))
time.sleep(5)

print("Now let's try to replace \"i\" with \"&\" in \"Zen of Python\"")
time.sleep(10)

print(s.replace('i', '&'))

print("Second part of the 3rd task HW3")
time.sleep(3)

n = int (input ("Input the four-digit natural number: "))

a = n% 10

b = (n // 10)% 10

c = (n // 100)% 10

d = (n // 1000)% 10

product = a * b * c * d

time.sleep(3)
print ("Product of the digits in number:", product)

time.sleep(3)
print("Reverse of the number:", str(a) + str(b) + str(c) + str(d))
time.sleep(3)

print("Let's sort the digits in number:")
sor = [a,b,c,d]
print(sorted(sor))

time.sleep(3)

print("Third part of the 3rd task HW3")

a = int(input("Input the number a:"))
b = int(input("Input the number b:"))

a =a+b
b =a-b
a =a-b

print("We need to swap these numbers")
time.sleep(3)

print("a = ", a)
print("b = ", b)