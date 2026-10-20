for i in range(0,10):
    if i==5:
        print("Five")
    else:
        print(i)

print("***************************************")
for i in range(0,10):
    print(i)
    if i==5:
        break

for i in range(0,10),1:
    if i==5 or i==6:
        print(i)
    else:
        pass

print("---------------------------------------------------")

for i in range(10):
    if i%2==0:
        print(i)

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
for i in range(10):
    if i%2!=0:
        print(i)

#continue -> skips the current iteration and moves to next iteration
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
for number in range(0,10):
    if number % 2 == 0:
        continue
    else:
        print(number)


#New Program
print("))))))))))))))))))))))))))))))))))))))")


for num in range(101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)