# executes a block of code while soem condition remains true

name =input("Enter name: ")

# if name == "":
#     print("No name")

# else:
#     print(f"Hello {name}")

# what if you want it to keep execute until a name is give

while name == "":
    print("No name")
    name =input("Enter name: ")
print(f"Hello {name}")