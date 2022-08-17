# Python Inheritance

# Syntax
# class BaseClass:
#     # Body o the base class
# class DerivedClass(BaseClass)
#     # Body of the derived class

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = []
        for i in range(no_of_sides):
            self.sides.append(0)

    def input_sides(self):
        for i in range(self.n):
            self.sides[i] = float(input("Enter sides"+str(i+1)+" : "))

    def display_sides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

p1 = Polygon(3)
p1.input_sides()
p1.display_sides()
