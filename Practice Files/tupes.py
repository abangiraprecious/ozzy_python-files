# A tuple () ordered and unchangeable
# - duplicates are okay
# - faster
# - useful for grouping together related data


student = ("Angel", "21", "female")

print(student.count("21")) # how many times something appears

print(student.index("female")) #indec of the value

for x in student:
    print(x)


if "Bro" in student:
    print("Angel is here")

else:
    print("Not here")