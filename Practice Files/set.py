# A set {}  is unordered is mutable because you can add/remove and immutable because what you add inside must be simple/unchangeable. Unordered means that it does track positioning in insertion sequence. So indices are out of the mix
# - no duplicates in that set. it ignores the duplicate
# - you can't put a list inside a set {[]} 


fruit = {"mangoe", "apple", "banana", "guava", "kiwi"}

print(len(fruit))

fruit.add("pineapple")

print(fruit)

fruit.remove("pineapple")

print(fruit)

fruit.pop() # randomly

print(fruit) 