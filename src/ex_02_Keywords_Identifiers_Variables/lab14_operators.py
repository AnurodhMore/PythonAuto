import math
#Arithmetic
from unicodedata import decimal

# +,-,*,/,//,%,**,   division always gives float value

#Comparison(Relational) operators > will give boolean answers
#==, !=, >, <, >=, <=

#Logical  operator

# AND, OR , NOT

# Assignment operator
#Bitwise operator

#membership operator
result = 'a' in 'apple'
print(result)

#identity operator

x = [1,2,3]
z = [1,2,3]
print(x is z)

#write a program to calculate area of a circle
p = 3.14
r =  float(input('Enter a radius: '))
area = p * pow(r,2)
print(f"Area of the circle is -> {area:.2f}")
# up to 2 decimal()

print(math.pi)
print(math.pow(2,2))
print(math.sin(90))
