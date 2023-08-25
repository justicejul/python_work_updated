# Write a loop that prompts the user to enter a series of 
# pizza toppings until they enter a 'quit' value. As they enter each topping, 
# print a message saying you’ll add that topping to their pizza.

# name = input("\nHello what is your name: ")
# if name != "":
# 	print(f"Hello {name}")
# else:
# 	print("Please, input your name")

# prompt = f"\n{name.title()}input your preference of pizza toppings"
# prompt += 'When you\'re done, input "quit" ' 

# while True:
# 	pizza = input(prompt)
# 	if pizza == 'quit':
# 		break
# 	else:
# 		print(pizza)

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