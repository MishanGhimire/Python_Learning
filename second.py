## Variables and Data Types  Python - Day #2
a = complex(8,2)
print(a)
a = 123
print(a)
a1 = 9

b = "Mishan"
print(b)
print(a + a1)
print("The type of a is", type(a))

## Challenge:
    ## Write a Python program that swaps the values of two variables without using a third variable.
a = 7
b = 10

print("Before swapping:")
print("a=", a)
print("b=",b)

a,b = b,a #implementing swap functiion here

print("After swapping:")
print("a=", a)
print("b=", b)