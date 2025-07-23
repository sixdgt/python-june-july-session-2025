# function
# Sum of Two Numbers
# Write a function add_numbers(a, b) that returns the sum of two numbers.
num_one = float(input("Enter first number: "))
num_two = float(input("Enter second number: "))

# this is type return function
# it will return the sum of two numbers
# we can use return statement to return the value from the function
# we can call the function and store the result in a variable
# Parameter: variables/values passed inside the parenthesis while defining the function
# Argument: variables/values passed inside the parenthesis while calling the function
def add_numbers(a, b):
    temp_sum = a + b
    return temp_sum
print("Case 1: sum of two numbers: ", add_numbers(num_one, num_two))
# to reuse the value or data return by the function, we can store it in a variable
result = add_numbers(num_one, num_two)
print("Result of addition: ", result)
# here the output is displayed using print function inside the function
# no return type function
def sum_of_two_numbers(a, b):
    temp_sum = a + b
    print("Case 2: Sum of two numbers: ", temp_sum)
# we can simply call the function to get the output
sum_of_two_numbers(num_one, num_two)

# function without parameters
def sum():
    print("Sum of two numbers is: ", num_one + num_two)
# if the function does not take any parameters, we can call it directly
sum()

# Check Even or Odd
# Write a function is_even(n) that returns True if the number is even, otherwise False.
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print("Is the number even? ", is_even(12))
output = is_even(13)
print(type(output))
print(output)

if output:
    print("The number is even.")
else:
    print("The number is odd.")

# we can also use ternary operator
print("Using ternary operator: ", "Even" if is_even(13) else "Odd")

# Factorial Calculation
# Write a function factorial(n) that returns the factorial of a given positive integer n.

# Find Maximum of Three Numbers
# Write a function max_of_three(a, b, c) that returns the largest among the three numbers.

# Count Vowels in a String
# Write a function count_vowels(s) that counts the number of vowels in a given string.

# Check Prime Number
# Write a function is_prime(n) that returns True if a number is prime, else False.

# Reverse a String
# Write a function reverse_string(s) that returns the reversed version of the input string.

# Check Palindrome
# Write a function is_palindrome(s) that checks if a string is a palindrome (same forwards and backwards).

# Generate Multiplication Table
# Write a function multiplication_table(n) that prints the multiplication table of n from 1 to 10.

# Find the Sum of a List
# Write a function sum_list(numbers) that returns the sum of all elements in a list.