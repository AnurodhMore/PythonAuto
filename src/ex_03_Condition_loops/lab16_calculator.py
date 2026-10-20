number = int(input("Enter a number: "))

if number > 0 and number < 100:
    if number >=90 and number <=100:
        print("A")
    elif number >=80 and number <=89:
        print("B")
    elif number >=70 and number<=79:
        print("C")
    elif number >=60 and number<=69:
        print("D")
    else:
        print("F")
else:
    print("Invalid input")
