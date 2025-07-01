# Operators in Python
# 1. Arithmetic Operators
# a. addition +
print("Addition - ", 50 + 30)

# b. subtraction -
print("Subtraction - ", 100 - 36)

# c. multiplication *
print("Multiplication - ", 12 * 12)

# d. division /
print("Division - ", 33 / 11)

# e. modulus %
print("Modulus - ", 35 % 11) # 2  - returns the remainder value

# f. floor division // - returns the quotient value
print("Floor Division - ", 35 // 11) # 3

# g. exponentiation ** - to the power of
print("Exponentiation - ", 2 ** 3) # equivalent to 2 * 2 * 2
# Note: in case of complex numbers - real number operates with real number and imaginary number operates with imaginary number
# example
print("Complex number - sum : ", (10 + 3j) + (12 + 6j))
# here 10 is real number whereas 3j is imaginary number

# in case of str if we use '+' operator then it will concatenate/combine the strings
print("String concatenation - ", "10" + "12") # here 10 and 12 both are strings so output will be 1012

# 2. Assignment Opeartors
# a. =
num = 10
# b. +=
a = 12
print("a = ", a)
a += 10 # equivalent to a = a + 10
print("a += 10 - ", a)

# similarly we have -=, *=, /=, %=, //=, **=
# case modulus 
x = 12
y = 2
print("x = ", x)
print("y = ", y)
x %= y # equivalent to x = x % y
print("x %=y ", x)

# 3. Comparative Operators
# a. ==
print("10 == 10", 10 == 10) # True
print("10 == 12", 10 ==12) # False

# b. !=
print("10 != 10", 10 != 10) # False
print("10 != 12", 10 != 12) # True

# c. >
print("10 > 12", 10 > 12) # False
print("10 > 9", 10 > 9) # True
print("10 > 10", 10 > 10) # False

# d. <
print("10 < 12", 10 < 12) # True
print("10 < 9", 10 < 9) # False
print("10 < 10", 10 < 10) # False

# e. >=
print("10 >= 12", 10 >= 12) # False
print("10 >= 9", 10 >= 9) # True
print("10 >= 10", 10 >= 10) # True

# f. <=
print("10 <= 12", 10 <= 12) # True
print("10 <= 9", 10 <= 9) # False
print("10 <= 10", 10 <= 10) # True

# 4. Logical Operators - operates with multiple statement
# a. logical and - all statement must be true otherwise it will return false
print("Logical and: (10 == 10) and (10 <= 12) - ", (10 == 10) and (10 <= 12)) # True
# here statement: (10 == 10) & (10 <= 12) both must return true in order return True
print("Logical and: (10 != 12) and (13 <= 12) and (12 <= 12) - ", (10 != 12) and (13 <= 12) and (12 <= 12)) # False

# b. logical or - if any of the statement is true then it returns True
print("Logical or: (13 < 14) or (13 <= 5) - ", (13 < 14) or (13 <= 5)) # True
print("Logical or: (13 >= 13) or (12 != 12) or (14 == 10) - ", (13 >= 13) or (12 != 12) or (14 == 10)) # True
print("Logical or: (13 >= 15) or (12 != 12) or (14 == 10) -", (13 >= 15) or (12 != 12) or (14 == 10)) # False

# c. logical not - reverse the output i.e if True then returns False and viceversa
print("Logical not: (10 == 10) and (10 <= 12) - ", not (10 == 10) and (10 <= 12)) # False
print("Logical not: (10 == 10) and (10 <= 12) - ", not ((10 == 10) or (15 <= 12))) # False

# case one:
username = "july"
password = "2025"
print(not (username != "july")) # suppose 'july' exist in database

# 5. Bitwise Operator
# a. Bitwise AND: &
num_one = 28
num_two = 15
print(num_one & num_two)
# b. Bitwise OR: |
print(num_one | num_two)
# Day 2 - Assessement one: try other bitwise operator
# Bitwise Shift (Left Shift and Right Shift), OR, XOR

# 6. Identity Operator
# a. is - checks identical values
discount_one = 12
discount_two = 25
discount_three = discount_one
print(discount_one is discount_two) # True
print(discount_one is discount_three) # True

# b. is not - reverse of is
print(discount_one is not discount_two)

students = ["Ram", "Shyam", "Hari"]
people = students
players = ["Ram", "Shyam", "Hari"]
print(students is people) # True
print(students is players) # False -> are cached in different memory location

# in case of integers
vat = 13
tax = 13
print(vat is tax) # True -> are cached in same memory location

# to check memory address we use id()
print("ID of vat: ", id(vat))
print("ID of tax: ", id(tax))
print("ID of students: ", id(students))
print("ID of players: ", id(players))
print("ID of people: ", id(people))

# Day 2 - Assessment Two - study membership
# Practice at least 7-8 examples of each operators
