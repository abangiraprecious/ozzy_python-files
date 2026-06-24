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