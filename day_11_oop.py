# Constructor Overloading
class Person:
    # constructor overloading is not directly supported in Python,
    def __init__(self, name, age, dob):
        self.name = name
        self.age = age
        self.dob = dob
    
    def __init__(self, name):
        self.name = name
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # method overloading
    def getInfo(self, name):
        self.name = name
        print(f"Name: {self.name}")
    
    def getInfo(self, name, age):
        self.name = name
        self.age = age
        print(f"Name: {self.name}, Age: {self.age}")
# creating object with multiple constructors
# p1 = Person("Alice", 30, "1993-01-01") # 
p2 = Person("Bob", 25)
# p3 = Person("Charlie")
# calling method with different parameters
# p2.getInfo("Mohan")
p2.getInfo("Hiraman Kaji", 23)    
# whenever we overload a method or constructor, python interpreter will give priority to the last defined method or constructor

# For this issue, we can implement variable-length arguments using *args or **kwargs
# for example
class Vehicle:
    def __init__(self, **kwargs):
        self.brand = kwargs.get('brand')
        self.color = kwargs.get('color')
        self.model = kwargs.get('model')
        self.year_made = kwargs.get('year_made')

# creating vehicle object
v1 = Vehicle(brand='Toyota', color='Red')
print("Vehicle Brand: ", v1.brand)
print("Vehicle Color: ", v1.color)