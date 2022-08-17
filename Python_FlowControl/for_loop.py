# For Loop

languages = ['Java', 'Python', 'C++']
for item in languages:
    print(item)

# other example.

# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for i in numbers:
    sum = sum + i

print("The sum is", sum)

# MUltiplication Table

n = 14
for i in range(1, 11):
    print(n, 'x', i, '=', n*i)

# Fo loop with else

my_list = [5, 'Hello']
for item in my_list:
    print(item)
else:
    print('Inside else')
