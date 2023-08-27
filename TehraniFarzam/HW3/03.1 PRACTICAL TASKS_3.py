# ====== interchange the value of two variable
#        without using the third variable        ======

a = input("a: ")
b = input("b: ")
a, b = b, a

print(f"After interchange: a is {a} and b is {b}")
print("___________________________________________")
#===== also: ======
c = 1
d = 2
c = c + d
d = c - d
c = c - d
print("c = 1 and d = 2. "f"After interchange: c is {c} and d is {d}")

