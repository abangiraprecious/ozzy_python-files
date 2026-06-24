# A set {}  is unordered is mutable because you can add/remove and immutable because what you add inside must be simple/unchangeable. Unordered means that it does track positioning in insertion sequence. So indices are out of the mix
# - no duplicates in that set. it ignores the duplicate
# - you can't put a list inside a set {[]} 


fruit = ["mangoe", "apple", "banana", "guava", "kiwi"]
print(fruit)
print(fruit[2])
print(fruit[:2]) #first two elements
print(fruit[::2]) #every 2nd element starting from 0 as the first element to be printed

# for x in fruit: #for every frui (x) in "fruit" variable
#     print(fruit)

print(len(fruit))

print("kiwi" in fruit) #Boolean

#reassigning
fruit[0] = "orange"

# for x in fruit: #for every frui (x) in "fruit" variable
#     print(fruit)

fruit.append("tangerine") #add to the end
fruit.remove("apple") 


print(fruit)

fruit.insert(0, "apple") #insert an element

print(fruit)

fruit.sort() #alphabetical order 
print(fruit)

fruit.reverse() #reversed in the order in which you placed them unless you first sort them
print(fruit)

fruit.clear()
print(fruit)

fruits = ["mangoe", "mangoe", "apple", "banana", "guava", "kiwi"]
print(fruits.index("guava"))#3

print(fruits.count("mangoe")) #2