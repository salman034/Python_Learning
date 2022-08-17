# Python Filter()

# The filter function extracts elements from an iterable(list, tuple etc).
# for which a function returns True.

# Example..

ages = [5, 12, 17, 18, 24, 32]

def MyClass(x):
    if x < 18:
        return False
    else:
        return True

adults = filter(MyClass, ages)
for x in adults:
    print(x)


# Another example Using Lambda Function Inside filter()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(new_list)


