# Encapsulation: data hiding and/or data binding
# to follow this rule, we use access modifiers
# 1. public - accessible from anywhere
# 2. protected - accessible from within the class and its subclasses
# 3. private - accessible only within the class

# to implement or make data accessible we use public methods i.e. getters and setters
# getters methods are used to access private data -> type return, takes no parameter
# setters methods are used to modify or store private data -> no return type but takes paramter
class Person:
    # public attributes
    name = "Himal Ghimire"
    # protected attributes
    _age = 30
    # private attributes
    __email = "himalgh@gmail.com"

    # creating getter and setter methods for private attributes
    def getEmail(self):
        return self.__email
    
    def setEmail(self, email):
        self.__email = email

p = Person()
print("Name: ", p.name)
print("Age: ", p._age)
# print("Email: ", p.__email) # after defining access modifer method still we cannot access private attributes directly
# to access we have to use method
print("Email: ", p.getEmail())
# to modify private attributes we can use setter method
p.setEmail("himalghimire@gmail.com")
print("Updated Email: ", p.getEmail())

p.name = "John Doe"  # public attribute can be modified directly