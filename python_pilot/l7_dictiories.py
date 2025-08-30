# Dictionaries - store data in key-value pairs

band = {"Vocals": "Plant", "guitar": "Page"}  # key : value

# dictonary constructor function
band2 = dict(Vocals="Plant", guitar="Page")  # (key="Value")

print(band)
print(band2)

print(type(band))
print(len(band))

# Access items
print(band["Vocals"])  # dictionary name plus the key results will be the value
print(band.get("Vocals"))  # use .get method and the key

# List all keys
print(band.keys())

# List all values
print(band.values())

# List of key/value pairs as tuples
print(band.items())

# verify if a key exits

print("guitar" in band)
print("matrix" in band)

# change values
band["Vocals"] = "Coverdale"  ## edits the key with new value
band.update({"Neo": "Matrix"})  # edits or introduces new key value pair

print(band)

# Remove items

print(band.pop("Vocals"))  # Removes item key-value pair and *returns the value

band.update({"Drums": "Bass"})
print(band)

print(
    band.popitem()
)  # method takes no argument, removes last key-value pair introduced, Returns tuple

# Delete and clear

band["Kurt"] = "Cobain"

del band["guitar"]
band2.clear()

print(band)
print(band2)

del band2

# copy dictionaries

# band2 = band  # creates reference not a copy, both will point to same thing

# print(band2)

band2 = band.copy()  # use copy method
band2.update({"Mama": "Mia"})
print(band2)

# use dict() constructor function to copy
band3 = dict(band)
band3["Trinity"] = "Matrix"
print(band3)

# Nested dictionaries - a dictinary that stores dictionaries

member1 = {
    "name": "Page",
    "Instrument": "guitar",
}  # member1 acts as a key for the key for the key value pairs
member2 = {"name": "Manly", "Instrument": "piano"}
member3 = {"name": "James", "Instrument": "Trumpet"}

band4 = {"member1": member1, "member2": member2, "member3": member3}

print(band4["member1"]["name"])  # finding a specific item on the nested dictionaries

# sets - store unordered homoginous data types, with no duplication

num = {1, 2, 3, 4}  # use carly {} braces
num3 = {1, 2, 3, 4}

num2 = set((2, 4, 8, 10))  # set constructor function set()

print(num)
print(num2)
print(type(num3))
print(len(num))

# True is a dupe of 1, false is a dupe of Zero

nums = {1, True, 2, 0, False, 3, 4, 0}  # comes in order and first come first *printed
print(nums)

# check if value is in a set
print(2 in nums)

# you can not refer to a number in a set with a key or an index positioning

# addig a new element to a set

nums.add(8)
print(nums)

# add elements from one set to another
morenums = {5, 6, 7}  # *
nums.update(morenums)
print(nums)
# you can use .update with lists, tuples, and dictionaries too. i.e where * is

# Merge 2 sets to create a new sets
one = {1, 2, 3}
two = {5, 8, 9}

mynewset = one.union(two)
print(mynewset)

# Keep only duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)

print(one)

# Keep everything except duplicates

one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
