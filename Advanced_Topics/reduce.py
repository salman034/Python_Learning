# Reduce Function in Python

from functools import reduce

number = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, number)
print('The sum of all number:', result)

number = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x * y, number)
print('The product of all number:',result)
