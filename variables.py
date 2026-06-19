# variables (rules that govern variables in python)

num1 = 100
num2 = 200

print(num1 + num2) #output: 300

# variable names should not start with a number
# variable names should not start with a capital letter
# variable names should not start with any special character...#,&,/,@, etc...
# a single variable name should not have spaces
# use relatable variable names

# a list is mutable data type. you can add/remove

fruits = ["mangoe", "apple", "dragonfruit"]
print(fruits[0])
print(fruits[2])
print(fruits[-3])
print(fruits.pop()) #pop removes the last element of the list
fruits.append("papaya") #adds to the end 

numbers = [1, 2, 3, [10, 20]] # the second list (inner) is in position 3. Rule of indices at work. To print 10 see below

print(numbers[3][0])

matrix = [[1,2,3], 
          [4,5,6], 
          [7,8,9]]

#so if i want to print six...

print(matrix[1][2])

matrix_two = [1,2,3,[10,20],30,[40,[60,70]]]

#to print 60

print(matrix_two[5][1][0])

# to print 70

print(matrix_two[5][1][1])