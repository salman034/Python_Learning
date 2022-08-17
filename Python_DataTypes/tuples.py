# Tuples

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])
print(my_tuple[4])

print(my_tuple[-1])
print(my_tuple[-4])

# Slicing

my_tuple = ('p', 'y', 't', 'h', 'o', 'n')

print(my_tuple[1:4])
print(my_tuple[:-4])
print(my_tuple[:])

# Changing tuple element

my_tuple = (1, 2, 3, 4, 5)
#my_tuple[0] = (1)

my_tuple = (1, 2, ['z', 'b'])
my_tuple[2][0] = 'a'
print(my_tuple)


# Using + and * Operators

odd = (1, 3, 5)
print(odd + (9, 11, 13, 15))

print(('a', 'b') * 3)


# Delete iems from a tuple

# my_list = ['s', 'a', 'l', 'm', 'a', 'n']
# del my_tuple[3] # TypeError: 'tuple' object doesn't support item deletion
# print(my_tuple)




