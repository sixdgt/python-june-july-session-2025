# Inheritance
class Shape:
    def __init__(self, **kwargs):
        self.side = kwargs.get('side')
        self.area = kwargs.get('area')
        self.perimeter = kwargs.get('perimeter')
    
    def calculateArea(self):
        return self.area
    
    def calculatePerimeter(self):
        return self.perimeter

class Circle(Shape):
    def __init__(self, **kwargs):
        super().__init__(side=kwargs.get('side'))
        self.radius = kwargs.get('radius')
        self.area = 3.1428 * self.radius**2 # accessing parent class attribute
        self.perimeter = 2 * 3.1428 * self.radius

# creating Circle object
c1 = Circle(radius=12, side=0)
print("Area of cirlce: ", c1.calculateArea()) # accessing parent class method
print("Perimeter of circle: ", c1.calculatePerimeter())
    
class Rectangle(Shape):
    def __init__(self, **kwargs):
        super().__init__(side=kwargs.get('side')) # accessing parent class constructor
        self.length = kwargs.get('length')
        self.breadth = kwargs.get('breadth')
        self.area = self.length * self.breadth
        self.perimeter = 2 * (self.length + self.breadth)

# creating Rectangle object
r1 = Rectangle(length=10, breadth=5, side=0)
print("Area of rectangle: ", r1.calculateArea()) # accessing parent class method
print("Perimeter of rectangle: ", r1.calculatePerimeter())

# Please create a solution of the case study using OOP
# types of inheritance
# 1. single inheritance
# 2. multiple inheritance
# 3. multilevel inheritance
# 4. hierarchical inheritance
# 5. hybrid inheritance

class GrandFather:
    def getGrandFatherInfo(self):
        print("This is GrandFather class")

class Father(GrandFather):
    def getFatherInfo(self):
        print("This is Father class")

class Son(Father):
    def getSonInfo(self):
        print("This is Son class")
    
# creating object of GrandFather - it carries self properties only
gf = GrandFather()
gf.getGrandFatherInfo()

# creating object of father - it carries self properties and GrandFather properties
f = Father()
f.getFatherInfo() # own method
f.getGrandFatherInfo() # inherited method from GrandFather

# creating object of Son - it carries self properties, Father properties and GrandFather properties
s = Son()
s.getSonInfo() # own method
s.getFatherInfo() # inherited method from Father
s.getGrandFatherInfo() # inherited method from GrandFather

# is-a relationship
# has-a relationship
