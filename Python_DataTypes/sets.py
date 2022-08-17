# Sets
#  A set is an unordered collecton of items.(No duplicates) and immutable.

# Different types of sets in Python
# set of integers
my_set = {1, 2, 2, 1, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3, 3)}
print(my_set)

# Add and Update sets

my_set = {1, 3}
print(my_set)

my_set.add(2)
print(my_set)


# Removing Element from a set

my_set = {1, 3, 5, 6, 7, 9}

my_set.discard(6)
print(my_set)

my_set.remove(1)
print(my_set)


# Set Union

A = {1, 2, 3}
B = {2, 3, 4, 5}
result = A | B
print('Result of union:',result)

result = B.union(A)
print(result)

# Set Intersection

A = {1, 2, 3}
B = {2, 3, 4, 5}
result = A & B
print('Result of Intersection',result)

result = B.intersection(A)
print(result)

# Set Difference

A = {1, 2, 3}
B = {2, 3, 4, 5}
result = A - B
print('Result of Difference:',result)
result = B - A

result = B.difference(A)
print(result)

