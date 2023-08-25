# Wrap your code from Exercise 10-6 in a while loop so the user can continue
# entering numbers even if they make a mistake and enter text instead of a number.
while True:
    Question_1 = input("\nDo you want to add numbers?: ")
    if Question_1.title() in ['Yeah', 'Yes', 'Y', 'yep', 'yea']:
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
            break
    else:
        break
