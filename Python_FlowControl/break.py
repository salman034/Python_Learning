# Break Statement.

number = [1, 5, 0, -4, 10, 9]
for value in number:
    if value < 0:  # condition to break
        break
    print(value)

# Continue Statement.

number = [1, 5, 0, -4, 10, 9]
for value in number:
    if value <= 0:
        continue
    print(value)