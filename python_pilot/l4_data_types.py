import math

# String data type

# literal assignement of value

first = "Dave"

last = "Gray"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function

# pizza = str("big homie")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# concatenation
# fullname = first + " " + last
# print(fullname)

# fullname += ""
# print(fullname)

# casting a number to a string

# decade = str(1980)
# print(type(decade))
# print(type(decade) == str)
# print(isinstance(decade, str))

# statement = "I like music from the" + " " + decade + ".s"
# print(statement)

# # multiple lines

ml = """

Hey, how are you?

folllow the white rabbit

                        The matrix has you

"""
# print(ml)

# Escaping special characters = \

# sentence = "i'm back at work!\tHey!\n"

# String Methods

# print(ml.title())  # proper case, capitalises every first letter in string
# print(ml.replace("rabbit", "wabbit"))

# print(len(ml))
# ml += "                      "
# ml = "                       " + ml
# print(ml)

# print(len(ml.strip()))
# print(len(ml.strip()))
# print(len(ml.strip()))
# print(len(ml))

# Build a Menu
# title = "menu".upper()
# print(title.center(20, "="))
# print("coffee".ljust(16, ".") + "1$".rjust(4))
# print("Muffin".ljust(16, ".") + "2$".rjust(4))
# print("Pancakes".ljust(16, ".") + "3$".rjust(4))
# print("Mashmellows".ljust(16, ".") + "4$".rjust(4))

# string index values
# print(first[1])
# print(first[-1])
# print(first[1:-1])
# print(first[1:])

# Some methods return boolean data
# print(first.startswith("D"))
# print(first.endswith("z"))

# Boolean data type
# myvalue = True
# x = bool(False)
# print(type(myvalue))
# print(isinstance(myvalue, bool))
# print(type(myvalue) == bool)

# numeric data types

# integer type
# price = 100
# b_price = int(80)
# print(type(price))
# print(type(price) == int)
# print(isinstance(b_price, int))

# float has a fraction or remainder

# Built-in functions for number
# gpa = 3.28
# print(abs(gpa))
# print(round(gpa))
# print(round(gpa, 1))


# print(math.floor(gpa))
# print(math.sqrt(50))

# casting string to a number

zipcode = "10010"
# zipcode = int(zipcode)
print(type(zipcode))
