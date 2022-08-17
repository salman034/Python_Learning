# While Loop

n = 3
i = 1
while i <= n:
    print("My loop is running")
    i = i + 1 # i is increased by 1

# infinite while loop

n = 3
i = 1
# while i <= n:
#     print("My loop is running") # In such case the body of while loop
                                  # is executed endlessly..

n = 10

# initialize sum and counter
sum = 0
i = 1
while i <= n:               #
    sum = sum + i
    i = i+1    # update counter
# print the sum
print("The sum is", sum)


# Multiplication Table
n = 12
i = 1
while i <= 10:
    print(n, 'x', i, '=', n*i)
    i = i + 1
