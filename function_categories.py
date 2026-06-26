# 1. User defined functions 
# - functions the user creates (sw engineer)

# 2. Inbuilt / predefined functions 
# - inbuilt in python. All you have to do is call them. 
#===================================|
# print()                           |  
# pop()                             |
# append()                          |
#these are inbuilt functions        |

# In each category, we have static and dynamic functions
# static - hard coded values. they will always give you the same value(s) when called upon.
# dynamic - will alyways give you different values each time it is called upon

def addition (num1, num2):
    print(num1 + num2)

#values you pass on to the parameters are called argumentsactual paremeters
addition(3, 6)


def subtract (num1, num2):
    print(num1 - num2)
subtract(3, 2) #1

def multiply (num1, num2):
    print(num1 * num2)
multiply(3, 2) #6

def divide (num1, num2):
    print(num1 - num2)
divide(4, 2) #2

def exponent (num1, num2):
    print(num1 ** num2)
exponent(3, 2) #9

def mod (num1, num2):
    print(num1 % num2)
mod(3, 2) #1


def userAdd():
    user_num = int(input("Number: "))
    user_num2 = int(input("Number 2: "))
    print(user_num + user_num2)
userAdd()