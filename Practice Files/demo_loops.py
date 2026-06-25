#suppose we are going to count to 5
for x in range (1,6): #first number is included, last number isn't. We stop at the number before it - it becomes the upper limit
    if x == 3: #yes
        continue #to skip over an iteration, use the continue key word
    else:
        print(x)


for x in range (1,6):
    if x == 5:
        break #stop
    else:
        print(x) 