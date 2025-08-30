# When a function calls its self.
def add_one(num):

    if num >= 9:
        return num + 1

    total = num + 1
    print(total)
    # The recursive function (calling it self)
    return add_one(total)


newTotal = add_one(0)

print(newTotal)
