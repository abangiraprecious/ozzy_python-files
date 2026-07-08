# for loops: execute a block of code a fixed number of times. You can iterate over a range, string, sequence, etc

#count to 10

for x in range(0,11): #where to begin, where to stop
    print(x)

print("Happy New Year")

alphabet = ("a", "b", "c", "d",)

for letters in alphabet:
    print(letters)

for letters in reversed(alphabet):
    print(letters)


for x in reversed(range(0,11)): #where to begin, where to stop
    print(x)

print("Happy New Year")



for x in range(7,11): #where to begin, where to stop
    print(x)


# add the step
for x in range(1,11,2): #where to begin, where to stop, count by this number
    print(x)

#iterate over string

credit_card = "1234-3455-3454-4564"

for x in credit_card:
    print(x)

name = "Michaela"

for letter in name:
    print(letter)

for letter in reversed(name):
    print(letter)

#suppose we are going to count to 26

for x in range (1,6):
    if x == 3:
        continue #to skip over an iteration, use the continue key word
    else:
        print(x)

for x in range (1,6):
    if x == 3:
        break #stop
    else:
        print(x)