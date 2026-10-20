age = int(input("Enter your age : "))

if age<=0 or age>130:
    print("Enter a valid age")
else:
    if age >= 21:
        print("You can go to the club")
    else:
        print("You cannot go to the club")


num = int(input("Enter a number: "))
if num>0:
    if num%2==0:
        print("Even number")
    else:
        print("Odd number")

else:
    print("Negative number")



no1 = int(input("Enter  number 1: "))
no2 = int(input("Enter  number 2: "))
no3 = int(input("Enter  number 3: "))

if no1>=no2 and no1>=no3:
    print(no1)
elif no2>=no3 and no2>=no1:
    print(no2)
else:
    print(no3)

