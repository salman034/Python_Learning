# Python List.

#  In Python, a list is created by placing elements inside square brackets [], separated by commas.

# Creating Emptylist
list1 = []

# List of Integers
list2 = [1, 2, 3]

# List with mixed data types
list3 =[1, 'Hello', 3.4]

# Accessng elements from a list

numbers = [1, 44, 10, 100, 3.33]

print(numbers[0])
print(numbers[4])
print(numbers[3])

# Negative indexing

number = [1, 44, 10, 100, 3.33]

print(number[1])
print(number[-4])
print(number[-3])


# Slicing of a list

number = [1, 44, 10, 100, 3.33, 66]

print('elements 3rd to fifth:',number[2:5])

print(number[3:])
print(number[:-5])
print(number[:]) # elements begining to end

# Change items of a list

odd = [ 2, 4, 6, 8]
odd[0] = 1
print(odd)

odd[1:4] = [3, 5, 7]
print(odd)


# Add elements to a list

odd = [1, 3, 5, 7]
odd.append(9)
print(odd)

odd = [1, 3, 5, 7]
odd.extend([9, 11, 13])
print(odd)


# Using + and * Operators

odd = [1, 3, 5]
print(odd + [9, 11, 13, 15])

print(['a', 'b'] * 3)

odd = [6, 9]
odd.insert(1, 3)
print(odd)


# Delete iems from a list

my_list = ['s', 'a', 'l', 'm', 'a', 'n']
del my_list[3]
print(my_list)

del my_list[1:5]
print(my_list)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list.remove(1)
print(my_list)

print(my_list.pop(1))
print(my_list)

print(my_list.pop())
print(my_list)

my_list.clear()
print(my_list)
