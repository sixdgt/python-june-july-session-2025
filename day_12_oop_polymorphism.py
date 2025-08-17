# Static Type or Compile-time Polymorphism
# overloading methods or constructors : directly not supported in Python

# Dynamic Type or Run-time Polymorphism
# method overriding : supported in Python
# method overriding: it is a concept of OOP where a child class overrides or defines a method with same name that is already defined in its parent class but the overriden method has different purpose or functionality.
class Animal:
    def speak(self):
        return "I am an animal and I can create sound to speak"

class Cat(Animal):
    def speak(self):
        return "I am a cat and I can create sound i.e. meow"

class Dog(Animal):
    def speak(self):
        return "I am a dong and I can create sound i.e. bark"

c = Cat()
d = Dog()
print("Cat Speak:", c.speak())
print("Dog Speak:", d.speak())

class Shape:
    def area(self):
        return "I can calculate area of a shape"
    
    def perimeter(self):
        return "I can calculate perimeter of a shape"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    # overriding area method
    def area(self):
        return 3.1428 * self.radius**2

    def perimeter(self):
        return 2 * 3.1428 * self.radius

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
            
    # overriding area method
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)

c1 = Circle(5)
r1 = Rectangle(4, 5)

print("Circle Area:", c1.area())
print("Circle Perimeter:", c1.perimeter())
print("Rectangle Area:", r1.area())
print("Rectangle Perimeter:", r1.perimeter())

# checking behavior of overridden methods
shapes = [Circle(6), Rectangle(12, 7)]
for shape in shapes:
    print("Calculating area: ", shape.area())
    print("Calculating perimeter: ", shape.perimeter())