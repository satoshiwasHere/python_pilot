# global scope - availlable to all the code
# global keyword used to modify a variable used locally inside a function
# nonLocal key word used to access a variable in the parent function
name = "dave"
count = 1


def greeting():  # function has a local scope
    color = "blue"
    count = 3  # cant modify a global value locally, this is read like a variable
    print(color)
    print(name)


greeting()
