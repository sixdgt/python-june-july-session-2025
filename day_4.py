# Loops in python - to perform any task repeatedly

# 1. For Loop

places = ['Dharan', 'Kathmandu', 'Lalitpur', 'Pokhara']

for name in places:
    print("Cities in Nepal: ", name)

# range() - to generate a sequence of numbers between a given range
for num in range(2, 17): # no jumping value so it will increment by 1
    print("Generating numbers: ", num)

for num in range(15): # no starting value so it will start from 0 and increment by 1
    print("Generating numbers: ", num)

for num in range(3, 34, 5): # starting value is 3, ending value is 34 and jumping value is 5
    print("Generating numbers: ", num)

# range() with for loop to access list elements
# len() - returns the length of a list
print("Length of places list: ", len(places))
print(places[0])
print(places[1])
for index in range(len(places)):
    print("Index: ", index, " Place: ", places[index])
# places[0]
# places[1]
# places[2]

# 2. While loop
# while loop - to repeat a block of code as long as a condition is true

items = ('Pencil', 'Pen', 'Eraser', 'Sharpener')

while 'Box' in items: # condition is false so it will not execute the block
    print("Items available: ")
    break

while 'Pencil' in items: # condition is true so it will execute the block
    print("Items available: ") # here we need to break the loop otherwise it will run infinitely
    break

# continue statement - to skip the current iteration and continue with the next iteration
for i in range(10):
    print("Current number: ", i)
    if i == 7:
        print("Skipping number 7")
        continue
        print("This will not be printed because of continue")
    print("Number after skipping 7: ", i)


count = 0
while count < len(items):
    print("Count is: ", count)
    print("Items :", items[count])
    count += 1

count = 0
while count < 4:
    print("Count is: ", count)
    print("Items :", items[count])
    count += 1

# 3. do while loop - python does not have a do while loop

# nested loops - loops inside a loop

odd = [1, 5, 7]
even = [4, 8, 12, 18, 36]

for num1 in odd:
    print("Odd number: ", num1)
    for num2 in even:
        print("Even number: ", num2)


whole_num = [
    (1, 3, 5), (2, 4, 6, 7, 8, 0), (11, 12, 13, 14), (100, 102, 105)
    ]

print("Length of whole number ", len(whole_num)) # it will give length of whole_num
print("First tuple: ", whole_num[0])
print("First tuple length: ", len(whole_num[0])) # it will give length of first tuple
print("Second tuple: ", whole_num[1])
print("Second tuple length: ", len(whole_num[1])) # it will give length of second tuple
print("Third tuple: ", whole_num[2])
print("Third tuple length: ", len(whole_num[2])) # it will give length of third tuple
print("Forth tuple: ", whole_num[3])
print("Forth tuple length: ", len(whole_num[3])) # it will give length of fourth tuple

for whole_num_data in whole_num:
    print("Whole number data: ", whole_num_data)

whole_num = [
    (1, 3, 5), (2, 4, 6, 7, 8, 0), (11, 12, 13, 14), (100, 102, 105)
    ]

for whole_num_index in range(len(whole_num)):
    print("Whole number index: ", whole_num_index, " Data: ", whole_num[whole_num_index])
    for tuple_data_index in range(len(whole_num[whole_num_index])):
        print("Tuple data index: ", tuple_data_index, " Data: ", whole_num[whole_num_index][tuple_data_index])
    
# pass statement - to skip the current iteration without executing the block
for i in range(10):
    pass

# function demo:
# syntax of function

# def function_name(parameters):
# function body

# def function_name(*args)
# def function_name(**kwargs)

print("Welcome to our online python session - CodeSandesh") # display this message more than 5 times
print("Welcome to our online python session - CodeSandesh")
print("Welcome to our online python session - CodeSandesh")
print("Welcome to our online python session - CodeSandesh")
print("Welcome to our online python session - CodeSandesh")
print("Welcome to our online python session - CodeSandesh")

# if we want to use or reuse any block of code for multiples times then we can use function
def welcome_message():
    print("Welcome to our online python session - CodeSandesh")
# to execute the function we need to call/invoke the function
# we call the function by its name
welcome_message()
welcome_message()
welcome_message()
welcome_message()
welcome_message()

print("using welcome message repeatedly")
for i in range(5):
    welcome_message()


print("Nested for loop example")

whole_num = [
    (1, 3, 5), (2, 4, 6, 7, 8, 0), (11, 12, 13, 14), (100, 102, 105)
    ]

print("Whole number data: ", whole_num)
print("Whole number index 0: ", whole_num[0])
print("Whole number index 1: ", whole_num[1])
print("Whole number index 2: ", whole_num[2])
print("Whole number index 3: ", whole_num[3])

for i in range(len(whole_num)):
    print("Whole number data with index: index is: ", i, " Data is: ", whole_num[i])
    temp_data = whole_num[i]
    print("Temporary data: ", temp_data)
    print(type(temp_data))
    for j in range(len(temp_data)):
        print("Temporary data of Whole number with index: index is: ", j, " Data is: ", temp_data[j])