# One common problem when prompting for numerical input occurs when people provide text instead of numbers.
# When you try to convert the input to an int, you’ll get a ValueError.
# Write a program that prompts for two numbers.
# Add them together and print the result.
# Catch the ValueError if either input value is not a number, and print a friendly error message.
# Test your program by entering two numbers and then by entering some text instead of a number.

Question_1 = input("Do you want to add numbers?: ")
if Question_1.title() in ['Yeah', 'Yes', 'Y']:
    print("You're going to give me two numbers")
    num1 = input("Give me the first number: ")
    if num1 != "":
        num2 = input("Give me the second number: ")
    else:
        num2 = input("you have to give a second number\nWhat is your second number:")

    try:
        num3 = int(num1) + int(num2)
    except ValueError:
        print("please put in numbers only!")
    else:
        print(num3)
