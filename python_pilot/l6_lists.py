# List - a collection of data types,
# holds mutiple values,
# referenced by a common name

users = ["Neo", "John", "Sara"]  # use [] braces

data = ["Bond", 101, True]

emptylist = []

# print("Neo" in data)

# print(users[0])
# print(users[-1])
# print(users[-2])

# print(users.index("Sara"))

# print(users[0:2])
# print(users[1:])

# print(len(users))

users.append("Morpheus")

print(users)

users += data

users.extend(data)

users.insert(0, "Durden")

print(users)

users[0:0] = ["Durden", "Tyler"]  # does not replace

users[1:3] = ["james", "Doe"]  # replaces items on the provided position i.e slicing

users.remove("Bond")
users.remove("Bond")
users.pop()
# print(users)

del users[0]

print(users)

# del data

data.clear()

print(data)
users.remove(101)
users.remove(101)
users.remove(True)


users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
# nums.sort(reverse=True)
# print(nums)

print(
    sorted(nums, reverse=True)
)  # global sorted function returns sorted list, without modifying it

numscopy = nums.copy()  # .copy function makes a copy of list
mynums = list(nums)  # use constructor function to make copy
copy_nums = nums[:]  # strips the whole list and make copy

print(type(nums))

mylist = list([1, "Neo", True])  # create list with constructor function
print(mylist)

# Tuples
# A tuple in Python is an ordered, immutable collection of elements that can hold items of different data types
# use curved () braces

mytuple = tuple(("dave", 42, True))  # tuple constructor function

tuple_2 = (1, 2, 4, 7)
alist = [3, 4, 17]

print(type(tuple_2))
print(type(alist))

# to manuplate tuple use list() costructor function , make change, then use tuple() function to convert to tuple.
# The initial tuple will remain unchanged. a 2nd tuple will emurge with the changes

n_list = list(mytuple)
n_list.append("Trinity")
n_tuple = tuple(n_list)

print(type(n_tuple))
print(n_tuple)

# unpacking a tuple
(folow, white, *rabbit) = tuple_2

print(*rabbit)

# dot notation

print(tuple_2.count(2))
