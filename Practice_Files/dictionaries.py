# a collection of {key:values} pairs
# - ordered and changeable
# - no duplicates allowed

capitals = {"Uganda":"Kampala",
            "Kenya" : "Nairobi",
            "Rwanda" : "Kigali",
            "Egypt" : "Cairo"}

print(capitals.get("Uganda")) # to print the value

capitals.update({"Ethiopia":"Addis"})

#you can remove a pair

capitals.pop("Kenya")

capitals.popitem() #removes the latest

#to get all keys alone

print(capitals.keys())

print(capitals)

#to get all keys alone

print(capitals.keys())

#to get all keys alone

print(capitals.values())


keys = capitals.keys()

for key in capitals.keys(): #iterate over every key
    print(key)