# Write a function called welcome that takes no parameters and prints "Welcome to Uganda".

def welcome():
    print("Welcome to Uganda")
welcome()

# Write a function called double that takes one number and returns that number multiplied by 2. Call it with the number 8 and print the result

def double(a):
     return a * 2

answer = double(8)
print(answer)

# Write a function called full_name that takes first and last as parameters and returns them combined with a space in between. Call it with your own name and print the result.

def full_name(first, last):
     return (first + " " + last)
name = full_name("Kwagala", "Grace")
print(name)

#15

#Write a function called area that takes length and width and returns the area. Then call it twice with different values, store both results in variables, and print the total of the two areas.

def area(l, w):
     return l * w
area1 = area(2, 2)
area2 = area (3, 4)


print(f"Area One is: {area1}")
print(f"Area Two is: {area2}")

summation = area1 + area2
print(sum)

# Calling a function inside a function: Write two functions: square(n) that returns n * n, and sum_of_squares(a, b) that uses square to return the sum of the squares of a and b. Call sum_of_squares(3, 4) and print the result. (Should print 25.)

def square(n):
     return n * n

def sum_of_squares(a, b):
     return square(a) + square(b)

print(sum_of_squares(3, 4))
