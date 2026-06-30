# Abangira Precious Nimmusiima

def register_student():
    name = input("Enter Your Full Name: ")
    age = int(input("How old are you: "))
    location = input("What is your address: ")
    phone_no = input("Enter Your Phone Number (0771234567): ")

    while len(phone_no) != 10:
        print("Digits are not 10")
        phone_no = input("Enter The Correct Phone Number (10 digits): ")

    track = input("Enter Your CSE Track (Python/Javascript): ")
    intake = input("What intake are you applying for: ")

    if age < 15:
        print("Unfortunately, you are not eligible because you are below 15 years")
    elif track.lower() not in ["python", "javascript"]:
        print("You are not eligible for CSE because your track is invalid.")
    else:
        print(f"Dear {name}, you are eligible for CSE because you are above the age of 15 and your track is {track} which is part of CSE! We will send you an email very soon confirming your admission.")

register_student()