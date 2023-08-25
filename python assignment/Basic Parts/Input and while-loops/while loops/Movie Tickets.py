# A movie theater charges different ticket prices depending on a person’s age. 
# If a person is under the age of 3, the ticket is free; if they are between 3 and 12, 
# the ticket is $10; and if they are over age 12, the ticket is $15. 
# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

# name = input("Name please ? :) ")
# if name != "":
# 	print(f"Hello {name}!")
# else:
# 	print("Please put in your name.")

# Age = input(f"{name.title()} How old are you? ")

# while True:
# 	if Age < 3:
# 		print(f"{name}, your ticket is for free!")
# 	elif Age == 3 and Age <= 12:
# 	    print(f"{name}, your ticket will be $10")
# 	elif Age > 12:
# 	    print(f"{name}, your ticket will be $15") 




# while True:
#     name = input("Name please ? :) ")
#     if name == "quit":
#         break
#     if name != "":
#         print(f"\nHello {name}!")
#     else:
#         print("\nPlease put in your name.")

#     Age = input(f"\n{name.title()} How old are you? ")
#     if Age != "" and Age != "quit":
#         Age = int(Age)
        
#         if Age < 3:
#             print(f"\n{name}, your ticket is for free!")
#         elif Age == 3 and Age <= 12:
#             print(f"\n{name}, your ticket will be $10")
#         elif Age > 12:
#             print(f"\n{name}, your ticket will be $15") 
#     else:
#         break




while True:
    name = input("Name please ? :) ")
    if name == "quit":
        break
    if name != "":
        print(f"\nHello {name}!")
    else:
        print("\nPlease put in your name.")

    Age = input(f"\n{name.title()} How old are you? ")
    if Age != "quit" and Age != "":
        Age = int(Age)
        
        if Age < 3:
            print(f"\n{name}, your ticket is for free!")
        elif Age <= 12:
            print(f"\n{name}, your ticket will be $10")
        elif Age > 12:
            print(f"\n{name}, your ticket will be $15") 
    else:
        break