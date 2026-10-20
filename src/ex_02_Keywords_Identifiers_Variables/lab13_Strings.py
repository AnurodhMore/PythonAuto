#strings
from math import remainder

name = "Anurodh"

b = "k"  #also string, no concpet of character

print(type(name))
print(type(b))

print(len(name))
print(name.upper())
print(name.lower())

age = "55"
print(type(age))

age2 = 55
print(type(age2))

#escape sequnce
print("***************************************************")
print("Hello\nWorld")
print("Hello\tWorld") #tab
print("Hello\bWorld") #backslash

#dir = C:\Anurodh\n.txt
dir = r"C:\Anurodh\n.txt" # it will print sa it is ignoring the sequence
print(dir)

#take 3 user from input and perform sub, mul, div

n1 = float(input("Enter n1: "))
n2 = float(input("Enter n2: "))
n3 = float(input("Enter n3: "))

sub = n1 - n2 - n3
mul = n1 * n2 * n3
div = n1 / n2 /n3

print("The subtraction is : ", sub)
print("The multiplication is : ", mul)
print("The division is : ", div)

#Quotient and Remainder

no1 = float(input("Enter no1: "))
no2 = float(input("Enter no2: "))
quot = no1//no2
remainder = no1%no2
print("The quotient is : ", quot)
print("The remainder is : ", remainder)

#use divmod

q, r = divmod(no1, no2)
print("The quotient is : ", q)
print("The remainder is : ", r)