# while loop executes code while a condition is true

# value = 1
# while value <= 10:  # uses : like if statement
#     print(value)
#     if value == 5:
#         break
#     value += 1

# continue breaks the code cycle ie jump to next cycle when codition is met
# value = 1
# while value <= 10:  # uses : like if statement
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     value = str(value)
#     print("value is equal to " + value)

# For loop - iterates over a sequence,char, list, ditonaries, sets i.e collection data types

names = ["John", "sara", "Dave"]
# x is a random letter representing each value in a for loop as it cycles through
# for x in names:
#     print(x)

# for x in "Mississippi":
#     print(x)


# for x in names:
#     if x == "sara":
#         break
#     print(x)

# for x in names:
#     if x == "sara": # skips sara i.e stops current cycle and goes 2 the nex loop cycle
#         continue
#     print(x)

# in range starts from 0 unless specified otherwise, last number is not included
# for x in range(4):
#     print(x)


# for x in range(2, 4): # start and stop
#     print(x)

# for x in range(0, 8, 2):  # start, stop , steps(incriments)
#     print(x)
# else:
#     print("Follow the White Rabbit")

# Nested loop the main loop iterates its element individially for the nested
# e.g john codes john eats john sleeps
names = ["John", "sara", "Dave"]
actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action)

for action in actions:
    for name in names:
        print(name + " " + action)
