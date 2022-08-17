# Comparission operators

print(5 > 6)
print(6 > 5)
print(6 < 5)
print(6 == 5)
print(6 != 5)
print(6 >= 5)


# and Operators

a, b, c = 1, 2, 3
print(b>a and c>a) # True
print(c>a and c<b) # false


# or Operators

a, b, c = 1, 2, 3
print(b>a or c>a) # True
print(c>a or c<b) # false


# not Operators

x = 5
print(not (x != 5))
print(not (x == 5))