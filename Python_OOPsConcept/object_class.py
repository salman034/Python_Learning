# How to define a Class.

class MyNewClass:
    #methods and attributes
    pass

# Creating an object.

class MyClass:
    a = 10

    def func(self):
        return "Hello"

# instantiate an object
ob = MyClass()

print(ob.func())
print(ob.a)

# Creating Multiple objects

class MyClass:
    a = 10

    def func(self):
        return "Hello"

ob1 = MyClass()
ob2 = MyClass()

print(ob1.a)
print(ob2.a)

ob1.a = 0
ob2.a = 100

print(ob1.a)
print(ob2.a)


# Class Object

class MyClass:
    a = 10
    def func(self):
        print('Hello')

print(MyClass.a)


# Another Example

class Number:
    def add(self, a, b):
        return a+b

    def multiply(self, a, b):
        return a*b

# instantiate an object
n1 = Number()

sum = n1.add(2, 3)
print(sum)

product = n1.multiply(2, 3)
print(product)