# . Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 
#    that do each of the following at least once:
# •	 Use a conditional test in the while statement to stop the loop.
# •	 Use an active variable to control how long the loop runs.
# •	 Use a break statement to exit the loop when the user enters a 'quit' value.

# THE GOOD ONE

name = input("\nHello what is your name: ")
if name != "":
	print(f"\nHello {name}")
else:
	print("Please, input your name")

prompt = f"\n{name.title()}, please input your preference of pizza toppings"
prompt += '\nWhen you\'re done, input "quit" '

while True:
	pizza = input(prompt)
	if pizza == 'quit':
		break
	else:
		print(f"\nAdding {pizza}....")






# USING THE SIGNAL METHOD

# THE BAD ONE



# name = input("\nHello what is your name: ")
# if name != "":
# 	print(f"\nHello {name}")
# else:
# 	print("Please, input your name")

# prompt = f"\n{name.title()}, please input your preference of pizza toppings"
# prompt += '\nWhen you\'re done, input "quit" '

# active = True

# while active:
# 	pizza = input(prompt)
# 	if pizza == 'quit':
# 		break
# 	else:
# 		print(f"\nAdding {pizza}....")
# 	if pizza == 'i don\'t want pizza':
# 		active = False




#THE GOOD ONE

name = input("\nHello what is your name: ")
if name != "":
	print(f"\nHello {name}")
else:
	print("Please, input your name")

prompt = f"\n{name.title()}, please input your preference of pizza toppings"
prompt += '\nWhen you\'re done, input "quit" '

active = True

while active:
	pizza = input(prompt)
	if pizza == 'quit':
		active = False
	else:
		print(f"\nAdding {pizza}....")



# THE CONDITIONAL STATEMENT METHOD

# THE BAD ONES

# name = input("\nHello what is your name: ")
# if name != "":
# 	print(f"\nHello {name}")
# else:
# 	print("Please, input your name")

# prompt = f"\n{name.title()}, please input your preference of pizza toppings"
# prompt += '\nWhen you\'re done, input "quit" '


# while pizza != 'quit':
# 	pizza = input(prompt)
#     print(f"\nAdding {pizza}....")


# THE BAD ONE


# name = input("\nHello what is your name: ")
# if name != "":
# 	print(f"\nHello {name}")
# else:
# 	print("Please, input your name")

# prompt = f"\n{name.title()}, please input your preference of pizza toppings"
# prompt += '\nWhen you\'re done, input "quit" '

# pizza = ""
# while pizza != 'quit':
# 	pizza = input(prompt)

# 	# if pizza == "":
# 	# 	pizza = input(prompt)
#     #     print(pizza)



# THE GOOD ONE


name = input("\nHello what is your name: ")
if name != "":
    print(f"\nHello {name}")
else:
        print("Please, input your name")

prompt = f"\n{name.title()}, please input your preference of pizza toppings"
prompt += '\nWhen you\'re done, input "quit" '

pizza= ""
while pizza != 'quit':
    pizza = input(prompt)
    if pizza != 'quit':
        print(f"\nAdding {pizza}....")


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################



while True:
    name = input("Name please ? :) ")
    if name == "quit":
        break
    if name != "":
        print(f"\nHello {name}!")
    else:
        print("\nPlease put in your name.")

    Age = input(f"\n{name.title()} How old are you? ")
    if Age != "" and Age != "quit":
        Age = int(Age)
        
        if Age < 3:
            print(f"\n{name}, your ticket is for free!")
        elif Age == 3 and Age <= 12:
            print(f"\n{name}, your ticket will be $10")
        elif Age > 12:
            print(f"\n{name}, your ticket will be $15") 
    else:
        break





Active = True

while Active:
    name = input("Name please ? :) ")
    if name == "quit":
        Active = False
    if name != "":
        print(f"\nHello {name}!")
    else:
        print("\nPlease put in your name.")

    Age = input(f"\n{name.title()} How old are you? ")
    if Age != "" and Age != "quit":
        Age = int(Age)
        
        if Age < 3:
            print(f"\n{name}, your ticket is for free!")
        elif Age <= 12:
            print(f"\n{name}, your ticket will be $10")
        elif Age > 12:
            print(f"\n{name}, your ticket will be $15") 
    else:
        Active = False









# prompt = "Your name please :)"

# name = ""

# while True:
# 	if name != "quit" or name == "":
#     	name = input(prompt)
#     else:
#     	print("put in your fucking age bitch!!!")

     
        
#     if name != "":
#         print(f"\nHello {name}!")
#     else:
#         print("\nPlease put in your name.")

#     # Age = input(f"\n{name.title()} How old are you? ")
#     # if Age != "" and Age != "quit":
#     #     Age = int(Age)
        
#     #     if Age < 3:
#     #         print(f"\n{name}, your ticket is for free!")
#     #     elif Age <= 12:
#     #         print(f"\n{name}, your ticket will be $10")
#     #     elif Age > 12:
#     #         print(f"\n{name}, your ticket will be $15") 
#     # else:
#     #     Active = False




prompt = "\nYour name please :)"

name = ""

while True:
    if name != "quit" or name == "":
        name = input(prompt)
        
        if name != "":
            print(f"\nHello {name}!")
        else:
            print("\nPlease put in your name.")
            
        Age = input(f"\n{name.title()} How old are you? ")
        if Age != "" and Age != "quit":
            Age = int(Age)
            
            if Age < 3:
                print(f"\n{name}, your ticket is for free!")
            elif Age <= 12:
                print(f"\n{name}, your ticket will be $10")
            elif Age > 12:
                print(f"\n{name}, your ticket will be $15") 
        else:
            Active = False












































































