# Eugenia Ceinos
# UWYO COSC 1010
# Submission Date: 11/3/2024
# Lab 07
# Lab Section: 16
# Sources, people worked with, help given to: none
# I didn't know if I was allowed to use another while or a for loop in the first part

# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered

factorial = 1
max = 0
num = 0
upper_bound = ""
t = 0

while t != 1:
    if upper_bound == "":
        upper_bound = input("Write an upper bound: ")
    else:
        pass

    if upper_bound.isdigit():
        max = int(upper_bound)
        pass
    else:
        upper_bound = ""
        print("Only positive numbers please")

    if num != max and upper_bound.isdigit():
        num += 1
        factorial = num * factorial
    else:
        pass

    if num == max and upper_bound.isdigit():
        print(f"The result of the factorial based on the given bound is {factorial}")
        t = 1

print("*"*75)

# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 

num_sum = 0 
substraction = 0

while True:
    number = input("Integer values to sum them up, 'exit' to stop: ")
    if number[0] == "-":
        number = number[1:]
        if number.isdigit():
            substraction += int(number)
    elif number.isdigit():
        num_sum += int(number)
    elif number.lower() == "exit":
        num_sum = num_sum - substraction
        print(f"Your final sum is {num_sum}")
        break
    else:
        print("Only numbers or 'exit' to end the sum and get your result")

print("*"*75)

# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 



while True:
    first = 0
    second = 0
    operator = 0
    t = False
    total = 0
    calculate = input("Operand operator operand or 'exit' to leave: ")
    calculate = calculate.replace(" ", "")
    if calculate.lower() == "exit":
        break


    for i in range(len(calculate)):
        if calculate[i] == "-":
            operator = calculate[i]
            first = calculate[:i]
            n = i + 1
            second = calculate [n:]
        elif calculate[i] == "+":
            operator = calculate[i]
            first = calculate[:i]
            n = i + 1
            second = calculate [n:]
        elif calculate[i] == "/":
            operator = calculate[i]
            first = calculate[:i]
            n = i + 1
            second = calculate [n:]
        elif calculate[i] == "*":
            operator = calculate[i]
            first = calculate[:i]
            n = i + 1
            second = calculate [n:]
        elif calculate[i] == "%":
            operator = calculate[i]
            first = calculate[:i]
            n = i + 1
            second = calculate [n:]
        
    if first.isdigit() and second.isdigit():
        first = int(first)
        second = int(second)
        t = True
    else:
        print("Only operand operator operand or 'exit' please")

    if t:
        if operator == "+":
            total = first + second
        elif operator == "-":
            total = first - second
        elif operator == "/":
            total = first / second
        elif operator == "*":
            total = first * second
        elif operator == "%":
            total = first % second
        print("Your total is:",total)