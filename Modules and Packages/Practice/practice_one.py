# Import and use a built-in module  Use the math module to print the square root of 144.

import math

print(math.sqrt(144))
# Import a specific function. Use from ... import ... to import only the randint function from the random module. Use it to print a random number between 1 and 50.

from random import randint

print(randint(1,50))


# Problem 11 — What's wrong?This code gives an error. Why?
import random
print(randint(1, 10))
