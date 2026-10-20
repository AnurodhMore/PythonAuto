#function
#syntax
# Define/Declare
#call

def greet(name):
    print("Hello ",name)

#greet("Anu") #calling


def greet_first_last(first,last):
    print("Your full name is ", first,last)

greet_first_last("Anu","More")

def sum(a,b):
    return a+b

result = sum(1,2)
print(result)

 #multiple

def math_op(a,b):
     return a+b, a-b, a*b

sum,diff, mul = math_op(10,5)

print(sum,diff,mul)

def dis_in(name,role):
    print("Name is: ", name, " Role is : ",role)
dis_in("Anu","PM")