value = "y"
count = 0

while value:  # Implies while value = True
    count += 1
    print(count)
    if count == 5:
        break
    else:
        value = 0
        continue  # causes an evaluation before the loop exist
