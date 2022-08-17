# Python Exception Handling

def findReciprocal(value):
    try:
        print('value:', value)
        r = 1/value
        print("The reciprocal of", value, "is", r, "\n" )

    except:
       print("you cannot find reciprocal of", value, "\n")


findReciprocal("Hello")
findReciprocal(2)


# Another Example...
# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()


# Example: Raising Exceptions

a = int(input("Enter a positive integer: "))
try:
    if a <= 0:
        raise ValueError("Not a positive integer")
    print("You entered", a)

except ValueError as ve:
    print(ve)