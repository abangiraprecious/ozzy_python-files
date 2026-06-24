name = input("Enter Your Full Name: ")
age = int(input("Enter Your Full Age: "))
location = input("Enter Your Location: ")
phone_no = input("Enter Your Phone Number (0771234567): ")

while len(phone_no) != 10 :
    print("Digits are not 10")
    phone_no = input("Enter The Correct Phone Number (10 digits): ")

track = input("Enter Your Python Track: ")

intake = input("What intake are you in: ")


#In an if-elif-else block, Python checks conditions top to bottom.
# - The moment it finds the first True condition, it:mruns that block and then skips all the rest
if age < 15:
    print("You are not eligible because you are below 15 years")

elif track not in ("Python", "Javascript"):
    print("Not eligible for CSE because your track is invalid")

else:
    print(f"Dear {name}, you are eligible for CSE because you are above the age of 15 and your track is {track} which is part of CSE")






