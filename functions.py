# a function / routine is a named block of code that performs a specific task (one thing)
# a function in py is created with the use of the word "def" followed by a valid name of the function (must adhere to variable syntax)
# a function is self contained
# - variables within a function cannot be accessed out of that function by default

def stuff():
    num1, num2 = 10, 20
    print(num1 + num2) #if you run at this point, you will get no error and no output. The computer by default ignores that function until you call it. 
    # call a function by its name and parentheses
stuff() # function call, Technically, it is called a function invocation

num1, num2 = 10, 20 # here it doesn't have an identity. They are independent statements that don't have any identity
print(num1 + num2)

def add():
    num3, num4 = 2,4
    print(num3 + num4)
add()

def div():
    num3, num4 = 4, 2
    print(num3 / num4)
div()

def multiply():
    num3, num4 = 2,4
    print(num3 * num4)
multiply() #8

def modulus():
    num3, num4 = 7, 3
    print(num3 % num4)
modulus() #1

def subtract():
    num3, num4 = 4, 2
    print(num3 - num4)
subtract() #2

def exponet():
    num3, num4 = 4, 2
    print(num3 ** num4)
exponet() #16

 
