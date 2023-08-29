origin_number = 3264

#find product
a = origin_number
digit = a % 10
product = digit
a = a // 10
digit = a % 10
product = product * digit
a = a // 10
digit = a % 10
product = product * digit
a = a // 10
digit = a % 10
product = product * digit
print ("The product of the digits of", origin_number, "is:", product)

#reverse
b = str(origin_number)
print("Origin number is:",origin_number, "and reverse:", b[::-1])

#ascending order
b = str(origin_number)
c = sorted(b)
d = ''.join(c)
print ("Origin number is:", origin_number, "and ascending order:", d)


