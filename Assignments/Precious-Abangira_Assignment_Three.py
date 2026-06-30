


# Operators
# An operator is just a symbol that tells Python to do something with one or more values. For example, in "5 + 3", the "+" is the operator, and 5 and 3 are the values it works on.

print("OPERATORS")

# Arithmetic Operators - used for doing math
# +   add
# -   subtract
# *   multiply
# /   divide (always gives back a decimal)
# %   modulus - gives the remainder of a division
# **  exponent - raises a number to a power
# //  floor division - divides, then rounds down to a whole number

print("\nArithmetic Operators")
a = 10
b = 3

print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)
print("a % b  =", a % b)
print("a ** b =", a ** b)
print("a // b =", a // b)

# Comparison Operators - used to compare two values. These always give back True or False.
# ==  equal to
# !=  not equal to
# >   greater than
# <   less than
# >=  greater or equal
# <=  less or equal

print("\nComparison Operators")
x = 7
y = 10

print("x == y :", x == y)
print("x != y :", x != y)
print("x > y  :", x > y)
print("x < y  :", x < y)
print("x >= y :", x >= y)
print("x <= y :", x <= y)

# Logical Operators - used to combine conditions
# and  -> True only if BOTH sides are True
# or   -> True if AT LEAST ONE side is True
# not  -> flips True to False, or False to True

print("\nLogical Operators")
age = 20
has_id = True

print("age >= 18 and has_id :", age >= 18 and has_id)
print("age >= 18 or has_id  :", age >= 18 or has_id)
print("not has_id           :", not has_id)

# Assignment Operators - used to store or update a variable's value
# =   assign a value
# +=  add, then save - same as x = x + 3
# -=  subtract, then save - same as x = x - 3
# *=  multiply, then save - same as x = x * 3
# /=  divide, then save - same as x = x / 3

print("\nAssignment Operators")
score = 10
print("starting score:", score)

score += 5
print("after += 5:", score)

score -= 3
print("after -= 3:", score)

score *= 2
print("after *= 2:", score)

score /= 4
print("after /= 4:", score)


# Data Types
# A data type tells Python what kind of value a variable is holding. Python figures this out automatically based on what you assign.

print("\nDATA TYPES")

# int - a whole number, no decimal point

print("\nint")
students = 40
print("students =", students, "| type:", type(students))

# float - a number with a decimal point

print("\nfloat")
price = 9.99
print("price =", price, "| type:", type(price))

# str - text, written between quotes

print("\nstr")
name = "Alice"
greeting = "Hello, " + name + "!"
print("greeting =", greeting, "| type:", type(name))

# bool - only two possible values, True or False

print("\nbool")
is_passing = 60 >= 50
print("is_passing =", is_passing, "| type:", type(is_passing))

# list - an ordered collection you CAN change, written in [ ]

print("\nlist")
fruits = ["apple", "banana", "cherry"]
print("fruits =", fruits)
fruits.append("mango")
print("after append:", fruits)
fruits[0] = "kiwi"
print("after changing index 0:", fruits)

# tuple - an ordered collection you CANNOT change, written in ( ). Use a tuple when the data should stay fixed, like coordinates.

print("\ntuple")
coordinates = (10, 20)
print("coordinates =", coordinates)
print("x value:", coordinates[0], "| y value:", coordinates[1])

# dict - a collection of "key: value" pairs, written in { }. You look up values by their key instead of by position.

print("\ndict")
student = {"name": "John", "age": 20}
print("student =", student)
print("student's name:", student["name"])
student["age"] = 21
student["grade"] = "A"
print("after updates:", student)


# Conditional Statements
# Conditional statements let your program make decisions and run different code depending on whether something is True or False. The indented lines only run when the condition above them is True.

print("\nCONDITIONAL STATEMENTS")

# if - runs code only if the condition is True

print("\nif")
age = 20
if age >= 18:
    print("You are an adult.")

# if...else lets your code try one thing, and if that doesn't hold true, automatically fall back to doing something else instead, so the program always has a path to follow no matter what the condition turns out to be.

print("\nif...else")
age = 16
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")

# if...elif...else lets you line up several possible conditions and have Python check them one after another, top to bottom, stopping and running the matching block as soon as it finds the first one that's true, and falling back to else if none of them are.

print("\nif...elif...else")
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Grade: F")


# Loops
# A loop repeats a block of code multiple times, so you don't have to write the same instructions over and over manually.

print("\nLOOPS")

# for loop - repeats once for each item in a sequence

print("\nfor loop")
for i in range(5):
    print("i =", i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("fruit:", fruit)

# while loop - repeats as long as a condition stays True. Remember to update something inside the loop, or it never stops!

print("\nwhile loop")
count = 0
while count < 5:
    print("count =", count)
    count += 1

# Nested loops - a loop placed inside another loop. The inner loop runs all the way through for every single turn of the outer loop.

print("\nnested loops")
for row in range(1, 3):
    for col in range(1, 3):
        print(f"row {row}, col {col}")

# break and continue - control how a loop runs. break stops the loop completely, right away. continue skips just this one turn, then keeps looping.

print("\nbreak")
for number in range(1, 10):
    if number == 5:
        break
    print("number:", number)

print("\ncontinue")
for number in range(1, 6):
    if number == 3:
        continue
    print("number:", number)
