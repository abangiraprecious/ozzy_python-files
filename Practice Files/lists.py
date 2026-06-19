#1. Your favourite things

# Create a list called favourites with 4 of your favourite foods. Then print the first item and the last item.

favourites = ["my boyfried", "coffee", "fruit tea", "books"]
print(favourites[0])
print(favourites[3])

# Create a list of any 5 numbers. Print how many items are in it using a built-in Python function.

numbers = [1, 2, 3, 4, 5]
print(len(numbers)) #print the len (length) of said numbers

data = [1, 2, 3, [10, 20], 30]
print(data[3]) #10,20
print(data[3][0]) #10
print(data[3][1])# 20

mix = [100, [5, 10, 15], 200, [7, 8]]
print(mix[1][2]) #15
print(mix[-1][0])#7
print(mix[1][-1])#15

m = [1, 2, 3, [10, 20], 30, [40, [60, 70]]]
print(m[3][1]) #20
print(m[5][0]) #40
print(m[5][1]) #60,70

m = [1, 2, 3, [10, 20], 30, [40, [60, 70]]]
print(m[5][1][0])# 60
print(m[5][1][1])# 70
print(m[5][1][-1])# 70