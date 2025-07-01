# Day 1: basic python revision
name = 1
print(type(name))

address = "kathmandu Nepal"
print(type(address))

price = 120.58 
print(price)
print(int(price)) # type casting - converting one type to another
price = 2580.22
print(price)
# mutable : can be changed
# immutable : can't be changed
print(address)
print(address.upper()) # creates new reference
address_cap = address.upper()
print(address_cap)
print(address)

# note: python do not use {} to define scope
# instead it uses indentation to define scope
# indentation: single tab or 4 spaces
# variable re-declaration
num = 12
print("First - ", num)
if num > 10:
    print("second - ", num)
    # re-declaration
    num = 13
    print("Third -", num)

print("Fourth - ", num)

# in case function
discount = 15
print("Discount first - ", discount)
# fuunction declaration
def calculate_discount():
    # print("Discount Second - ", discount) - we cannot use before declaring
    discount = 15 * 0.1 # re-declaring variable
    print("Discount Third -", discount)

# function invocation
# the code inside function will not execute until and unless it is not called
calculate_discount()
print("Discount Fourth - ", discount)
# Note: if any variable is re-declared inside a function then we are allowed use
# it before declaring the variable

