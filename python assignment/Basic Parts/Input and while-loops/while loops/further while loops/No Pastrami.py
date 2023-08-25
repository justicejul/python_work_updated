# Using the list sandwich_orders from Exercise 7-8, make sure 
# the sandwich 'pastrami' appears in the list at least three times. Add code 
# near the beginning of your program to print a message saying the deli has 
# run out of pastrami, and then use a while loop to remove all occurrences of 
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up 
# in finished_sandwiches.

# sandwich_orders = ["panini", "cheese-steak", "pastrami", "ham", "pastrami", "cuban", "meatball", "pastrami", "pinwheel", "pastrami", "muffuletta"]

# print("Deli has run out of pastrami sandwiches")

# while sandwich_orders:
# 	if "pastrami" in sandwich_orders:
# 		sandwich_orders.remove("pastrami")


sandwich_orders = ["panini", "pastrami", "cheese-steak", "chicken ", "vegetable", "pastrami", "ham", "cuban", "meatball", "pinwheel", "pastrami", "ice-cream", "muffuletta", "pastrami"]
finished_sandwiches = []

print("Deli has run out of pastrami sandwiches")

while sandwich_orders:
	if "pastrami" in sandwich_orders:
		sandwich_orders.remove("pastrami")
	else:
		current_sandwiches = sandwich_orders.pop()
		print(f"\ni made your {current_sandwiches} sandwich")
		finished_sandwiches.append(current_sandwiches)
print("\n\n\n")

for finished_sandwich in finished_sandwiches:

	print(f"\nCome and get your {finished_sandwich} sandwich")