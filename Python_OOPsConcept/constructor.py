# Constructor

# Example problem

# Find Distance From Origin

class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distance(self):
        return (self.x**2 + self.y**2) ** 0.5

p1 = Point(6, 8)
distance = p1.distance()
print(distance)


# Another example of constructor

class Addition:
    first = 0
    second = 0
    answer = 0

    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second

obj = Addition(678, 907)
obj.calculate()
obj.display()