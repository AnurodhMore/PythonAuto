#set -> Unordered collection

a ={1,2,3}
b = {3,4,5}

print(a.union(b))

print(a.intersection(b))

print(a.difference(b))

print(a-b)
print(b-a)
print(a^b)

#map -> applies a function to each item in a list and
#returns a map object
numbers = [1,2,3,4,5]

def sq(x):
    return x**2

sq_all_numbers= list(map(sq,numbers))
print(sq_all_numbers)

#Filter -> Filters elements of an iterale using
#a condition (return only those that match True)
numbers = [1,2,3,4,5]

def even_no(x):
    return x%2==0

even_numbers = list(filter(even_no,numbers))
print(even_numbers)

#Dictonary -> an unordered , mutuable and indexed collection
#of key value paris, defined by curly braces


my_dict = {"name" : "Anu",
           "age" : 25,
           "role" : "SDET",
           "exp": 3 }

print(my_dict)
print(my_dict["name"])
print(my_dict["age"])

for key,value in my_dict.items():
  #  print(key)
   # print(value)
    print(key,value)

print("age" in my_dict)