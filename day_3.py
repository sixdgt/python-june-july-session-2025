# Conditional Statement
# 1. if statement
# in order to execute the code inside the statement the conditions must be true

age = 18
if age <= 19:
    print("You are teen")

# making it multiple conditions
age = 18
if age >= 13 and age <= 19:
    print("You are teen")

# 2. if else statement
age = 12
if age >= 17:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# case-requirement: age greater 16, citizen -> nepali, criminal_record -> clean
# to get input from user we use 'input()'
print("We are asking your details to check your eligibility for voting rights.")
print("Please enter the following details: ")
age = float(input("Enter you age: "))
citizen = input("Enter your nationality: ")
criminal_record = input("Do you have any criminal record? Please enter Y or N: ")
if age >= 16 and citizen == 'Nepali' and criminal_record == 'N':
    print("You are eligible to Vote.")
else:
    print("You are not eligible to Vote.")

# 3. if else if statement
# in python: elif statement
age = float(input("Enter your age: "))

if age <= 12:
    print("You are child.")
elif age <= 19:
    print("You are teenager.")
elif age <= 40:
    print("You are young Adult.")
elif age <= 60:
    print("You are adult.")
else:
    print("You are old age.")

# days
day_name = input("Enter any day in a week: ")
if day_name == "Sunday":
    print("First day of the week.")
elif day_name == "Monday":
    print("Second day of the week.")
elif day_name == "Tuesday":
    print("Third day of the week.")
elif day_name == "Wednesday":
    print("Fourth day of the week.")
elif day_name == "Thursday":
    print("Fifth day of the week.")
elif day_name == "Friday":
    print("Second last day or sixth day of the week")
elif day_name == "Saturday":
    print("Last day or seventh day of the week.")
else:
    print("Please enter correct day name.")

# 4. nested if statement
username = input("Enter you username: ")
pincode = int(input("Enter your pincode: "))
acc_no = input("Enter your account number: ")

if username == "binod":
    print("Welcome! ", username)
    if pincode == 4321:
        if acc_no == "AC001":
            print("Welcome to ABC Bank.")
        else:
            print("Invalid Account Number.")
    else:
        print("Invalid pincode..")
else:
    print("Not registered yet...")

# Day 3
# Assessment 1: Ternary Conditional Statement
# Assessment 2: find the grade of student according to his/her marks obtained

# there is no switch case statement supportable in python
# instead of it we use match-case
num = 3

match num:
    case 1:
        print("Number one")
    case 2:
        print("Number two")
    case 3:
        print("Number three")
    case _: # for other case except the defined case
        print("Other number")
