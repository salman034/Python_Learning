# Python Recursion

# A function that calls itself is known as a recursive function.
# And this process is known as recursion.

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))

#In the above example, factorial() is a recursive function as it calls itself.

# Another example.

def cal_sum(n):
    if n == 1:
        return 1
    else:
        return n + cal_sum(n-1)
sum = cal_sum(6)
print(sum)
