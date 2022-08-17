#Pyhon Function

# in this example, we will create a function to add two numbers.

def add_number(num1, num2):
    sum = num1 + num2
    print('sum=', sum)

add_number(5, -12)


# return statement

def add_numbers(num1, num2):
    sum = num1 + num2
    return sum

result = add_numbers(5, -12)
print('sum =', result)
