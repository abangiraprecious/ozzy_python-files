# executes a block of code while soem condition remains true

name =input("Enter name: ")

# if name == "":
#     print("No name")

# else:
#     print(f"Hello {name}")

# what if you want it to keep execute until a name is give

while name == "":
    print("No name")
    name =input("Enter name: ") #without something like this, you get an infinite loop
print(f"Hello {name}")

# q to quit

food = input("Favorite food: ")

while not food == "q": #can also be written as [while food != "q":]
    print(f"Your fave food is {food}")
    food = input ("Another favorite food: ")
print("bye")