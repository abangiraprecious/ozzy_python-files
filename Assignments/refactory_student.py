#Abangira Precious Nimmusiima

name = input("Enter Your Full Name: ")
age = int(input("Enter Your Full Age: "))
location = input("Enter Your Location: ")
phone_no = input("Enter Your Phone Number (0771234567): ")

# I added this while loop to test my learning but also because it is common to put incorrect phone numbers. So I used the while loop to determine that it does not happen and, it is also not an infinite loop. 
while len(phone_no) != 10 :
    print("Digits are not 10")
    phone_no = input("Enter The Correct Phone Number (10 digits): ") 

track = input("Enter Your CSE Track (Python/Javascript): ")

intake = input("What intake are you in: ")

if age < 15:
    print("Unfortunately, you are not eligible because you are below 15 years")

elif track.lower() not in ["python", "javascript"]:
    print("You are not eligible for CSE because your track is invalid.")

else:
    print(f"Dear {name}, you are eligible for CSE because you are above the age of 15 and your track is {track} which is part of CSE! We will send you an email very soon confirming your admission.")
