# Python Dictionary

# A dictionary  is an unordered collection of items (similar like sets).
# It has a key and values.

# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}


# Accessing  dictionary Element

person = {'name': 'Salman', 'age': 26}
person_name = person['name']
print(person_name)

person_age = person['age']
print(person_age)

# Access value using get()

my_person = {'name': 'Salman', 'age': 26}
person_name = my_person.get('name')
print(person_name)

person_age = my_person.get('age')
print(person_age)

# Changing and Adding Dictionary items

my_dict = {'Name': 'Salman', 'Age': 26}

# update value
my_dict['Age'] = 27

print(my_dict)

# add item
my_dict['Address'] = 'Downtown'
print(my_dict)

# Removing elements from Dictionary

squares_num = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares_num.pop(4))
print(squares_num)

# remove an arbitrary item, return (key,value)

print(squares_num.popitem())
print(squares_num)

# remove all items
squares_num.clear()
print(squares_num)

# Iterating throug a Dictionary

squares = {1:1, 3:9, 5:25}
for i in squares:
    print(squares[i])

