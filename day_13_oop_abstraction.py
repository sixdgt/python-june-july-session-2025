# Abstraction in Python
# functionality are exposed but the core implementation mechanism are hidden

# to define abstract class in python we use abc module and to define abstract methods we use @abstractmethod decorator
# we cannot instantiate i.e. create an object of an abstract class
from abc import ABC, abstractmethod
# abstract class
class Vehicle(ABC):
    # to define an abstract method
    # Note: abstract methods are bodyless methods which are implemented by child classes
    # bodyless means no implementation in the parent class
    # in python we have to use 'pass' statement to define an abstract method
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass
    
    # here no @abstractmethod decorator is used so this method is a non abstract method
    # so we dont need to implement it in the child class
    def model_type(self):
        print("This is a vehicle model type")

# v1 = Vehicle()  # this will raise an error because we cannot instantiate an abstract class

# creating a derived child class of an abstract class i.e Vehicle
# note: if any class inherits the properties of an abstract class then it must implement all the abstract methods of that class
class Car(Vehicle):
    # overriding / implementing the abstract methods of parent class
    # we dont need to use @abstractmethod decorator in the implemented child class methods since they are already defined in the parent class
    def start_engine(self):
        print("Car engine started")
    
    def stop_engine(self):
        print("Car engine stopped")

# creating an object of the child class
c1 = Car()
# calling the methods of the child class
c1.start_engine()  # Output: Car engine started
c1.stop_engine()   # Output: Car engine stopped
c1.model_type()    # Output: This is a vehicle model type
# Since abstract class can have both abstract and non-abstract methods therefore we cannot achieve 100% abstraction with abstract classes
# so to achieve 100% abstraction we can use interfaces
# unlike java, c++ python doest not have a concept of interfaces or interface keyword but
# we can achieve the same functionality using abstract classes
# for this we have to create all the methods inside interface as abstract methods

# creating an interface in python
class ShapeInterface(ABC):
    @abstractmethod
    def compute_area(self):
        pass

    @abstractmethod
    def compute_perimeter(self):
        pass

# creating a class that implements the interface
class Circle(ShapeInterface):
    def __init__(self, radius):
        self.radius = radius

    # overriding the abstract methods of the interface
    def compute_area(self):
        return 3.1428 * self.radius**2
    
    def compute_perimeter(self):
        return 2 * 3.1428 * self.radius

    def show_info(self):
        print("This is a circle class implementing ShapeInterface")

cr = Circle(12)
print(cr.compute_area())       # Output: 452.3904
print(cr.compute_perimeter())  # Output: 75.456
cr.show_info()                 # Output: This is a circle class implementing ShapeInterface