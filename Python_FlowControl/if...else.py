# Python if..Statement

#Example-1

number = 5
if number > 0:
    print(number, "is a positive number.")
print("This is always printed.")

#Example-2

number = -1
if number > 0:
    print(number, "is a positive number.")
print("This is also always printed.")


# Python if...else Statement
num = 0
# num = -5
# num = 0

if num >= 0:
    print("Positive")
else:
    print("Negative number")


# Python if...elif...else Statement

num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")



# Python Nested if Example.

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
