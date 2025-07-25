# *args - accepts a variable number of positional arguments

def show_dialogue(*args):
    for diaglogue in args:
        print(diaglogue)

# def show_dialogue(dialogue):
#     print(dialogue)
show_dialogue("Hello! I am a dialogue one.")
show_dialogue("Hello! I am a dialogue two.", "Hello! I am a dialogue three.")
show_dialogue("Hello! I am a dialogue four.", "Hello! I am a dialogue five.", "Hello! I am a dialogue six.")

# **kwargs - accepts a variable number of keyword arguments
def show_product_details(**kwargs):
    print("Product Details:", kwargs)
    for key, value in kwargs.items():
        print(f"Key: {key}: Value: {value}")

show_product_details(name="Tool Box", price=300.00, quantity=10, specification="Plastic, 10x10x5 inches")

# Write a function max_of_three(a, b, c) that returns the largest among the three numbers. take parameters as *args

# using built-in max() function
def max_of_three(*args):
    if len(args) != 3:
        print("Please provide exactly three numbers.")
    else:
        return max(args)
        # return max(args[0], args[1], args[2])

print("Maximum of three numbers (10, 20, 30):", max_of_three(10, 20, 30))
# index 0 = 10
# index 1 = 20
# index 2 = 30
# using custom hard-coded logic
def max_of_three_number(*args):
    if args[0] >= args[1] and args[0] >= args[2]:
        return args[0]
    elif args[1] >= args[0] and args[1] >= args[2]:
        return args[1]
    else:
        return args[2]

print("Maximum of three numbers (10, 20, 30):", max_of_three_number(10, 20, 30))
print("Maximum of three numbers (30, 20, 10):", max_of_three_number(30, 20, 10))
print("Maximum of three numbers (20, 30, 10):", max_of_three_number(20, 30, 10))

# taking inputs outside of the function
num_one = float(input("Enter first number: "))
num_two = float(input("Enter second number: "))
num_three = float(input("Enter third number: "))
print("Maximum of three numbers (input):", max_of_three_number(num_one, num_two, num_three))

# takings inputs as arguments
print("Maximum of three numbers (input as args):", max_of_three(float(input("Enter first number: ")), float(input("Enter second number: ")),float(input("Enter third number: "))))

# built-in functions
# len() - returns the length of an object
# type() - returns the type of an object
# max() - returns the largest item in an iterable or the largest of two or more arguments
# min() - returns the smallest item in an iterable or the smallest of two or more arguments
# range() - returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number
# print() - prints the specified message to the screen, or other standard output device

# sorted() - returns a sorted list of the specified iterable's elements
# example of sorted:
prices = [123, 432, 100, 999, 12, 872]
print("Sorted prices:", sorted(prices))
print("Sorted prices in reverse order:", sorted(prices, reverse=True)) # here prices is *args and reverse is a keyword argument

# we can use both *args and **kwargs in the same function
def show_user(*args, **kwargs):
    print("Details:")
    for arg in args:
        print("Arg data: ", arg)
    for key, value in kwargs.items():
        print(f"Key: {key}, Value: {value}")

show_user("Salman Khan", age=58)
# sum() - returns the sum of all items in an iterable, or the sum of two or more arguments
# round() - rounds a number to a specified number of decimal places
# example of round:
print("Rounded value of 3.14159 to 2 decimal places:", round(3.14159, 2))
print("Rounded value of 3.14159 to 3 decimal places:", round(3.14159, 3))
print("Rounded value of 3.14159 to 1 decimal places:", round(3.14159, 1))
print("Rounded value of 3.14159 to 0 decimal places:", round(3.14159, 0))

# some of the functions or methods of python data types ie. list, set, tuple, dict, str

# str - string methods
# example of str methods
msg = "I am from Kathmandu, Nepal."

# upper() and lower() - convert string to uppercase or lowercase
print("Uppercase:", msg.upper())
print("Lowercase:", msg.lower())

# startswith() and endswith() - check if string starts or ends with a specific substring
print("Starts with 'I am':", msg.startswith("I am"))
print("Starts with 'Kathmandu':", msg.startswith("Kathmandu"))
print("Ends with 'Nepal.':", msg.endswith("Nepal."))
print("Ends with 'Kathmandu':", msg.endswith("Kathmandu"))

# list - list methods
# example of list methods
fruits = ["Apple", "Banana", "Cherry", "Kiwi"]
print("Original list:", fruits)
# to add new fruit to the list
fruits.append("Mango") # will append "Mango" to the end of the list
print("List after appending 'Mango':", fruits)
# append with index
fruits.insert(2, "Orange")  # insert "Orange" at index 2
print("List after inserting 'Orange' at index 2:", fruits)

# remove() - removes the first occurrence of a specified value
# if there are multiple occurrences, it will remove the first one
places = ["Kathmandu", "Pokhara", "Lalitpur", "Bhaktapur", "Kathmandu"]
print("Original places list:", places)
places.remove("Kathmandu")  # removes the first occurrence of "Kathmandu"
print("Places list after removing first 'Kathmandu':", places)

# removing all occurrences of an item
places = ["Kathmandu", "Pokhara", "Lalitpur", "Bhaktapur", "Kathmandu"]
while "Kathmandu" in places:
    places.remove("Kathmandu")  # removes all occurrences of "Kathmandu"
print("Places list after removing all 'Kathmandu':", places)

# pop() - removes and returns the item at the specified index (default is the last item)
print("List after removing 'Banana':", fruits)
print("Popped item from the list:", fruits.pop())  # removes and returns the last
print("List after popping last item:", fruits)
# pop(index) - removes and returns the item at the specified index
print("Popped item from the list at index 2:", fruits.pop(2))  # removes and returns the item at index 2
print("List after popping item at index 2:", fruits)
