#decoartor in python are a way to modify the behaviour of a function or a
# cass without changing the code

def add_security(func):
    def wrapper():
        print("1. Before the function is called")
        print("2. Add helmet, gloves, license")
        func()
        print("3. After function is called")
        print("4. Secure driving")

    return wrapper()




@add_security
def drive_ola():
    print("Drive Ola")