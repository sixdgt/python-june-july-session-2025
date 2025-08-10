# class - a blueprint for creating objects
# attributes - characteristics of a class
# attributes - class variables

# methods - functionalities of a class

# we must follow the rules of identifiers for naming classes, attributes, and methods
# class name: always start with a capital letter
# we can simply follow pascal case for naming classes

# attributes -> either camel case or snake case
# methods -> snake case or camel case

# examples: countries, members, students, employees, etc.
# to name classes: singular nouns -> common or collective nouns
# to names attributes: adjectives
# to name methods: verbs or verb phrases

# we use class keyword to define a class
class Country:
    # attributes
    name = "Nepal"
    continent = "Asia"
    region = "South Asia"
    currency = "Nepalese Rupee"
    country_code = "NP"
    prime_minister = "KP Sharma Oli"

    # methods
    def getCountryInfo(self): # this method belongs to the class Country
        """
        This method gives the basic information about the country.
        """
        print(f"Country Name: {self.name} - Continent: {self.continent}") # self.name refers to the attribute of class Country
    
    def getCountryName(self):
        """
        This method returns the name of the country.
        """
        return self.name
    
    def setCountryName(self, param_name):
        """
        This method sets the name of the country.
        """
        self.name = param_name

# object - an instance of a class
nepal = Country()  # creating an object of class Country

# accessing attributes and methods via object
print("Name of the country: ", nepal.name)
print("Continent: ", nepal.continent)

# callling methods
nepal.getCountryInfo()

# updating the name of the coutry
# we can directly update by accessing the attribute if the attribute is public
nepal.name = "Nepal (Federal Democratic Republic)"
print("Updated Name of the country: ", nepal.getCountryName())

# updating the name of the country using setter method since we have already defined it
nepal.setCountryName("Federal Democratic Republic of Nepal")
print("Updated Name of the country: ", nepal.getCountryName())

# constructor - special method or magic method which builds or create an object
# if we do not define a constructor then python will create a default constructor after executing the program
# __init__() 

# simple example of class with constructor
class Employee:
    # constructor
    def __init__(self, param_name, param_age, param_designation, param_gender, param_shift):
        """
        This is a constructor which initializes the attributes of the class Employee.
        """
        self.name = param_name # here self.name is class attribute whereas param_name is the parameter passed to the constructor
        self.age = param_age
        self.designation = param_designation
        self.gender = param_gender
        self.shift = param_shift
    
    # method 
    def getEmployeeDetail(self):
        """
        This method returns the details of the employee.
        """
        return print(f"Name: {self.name}, Age: {self.age}, Designation: {self.designation}")

# if the constructor is defined with parameters then we must pass arguments while creating an object
emp = Employee('Mohan Dhimal', 24, 'Software Engineer', 'Male', 'Day Shift')
# accessing attributes and methods via object
print("Employee Name: ", emp.name)
print("Employee Age: ", emp.age)
print("Employee Designation: ", emp.designation)
