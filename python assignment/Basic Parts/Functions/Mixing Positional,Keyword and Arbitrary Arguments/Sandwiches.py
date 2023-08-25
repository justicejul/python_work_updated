# Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function. 
# call provides, and it should print a summary of the sandwich that’s being ordered. 
# Call the function three times, using a different number of arguments each time.

def make_sandwich(name_of_sandwich, *ingredients):
	"""Type of a sandwich, and ingredients used in making it."""
	print(f"\n\nThis is a {name_of_sandwich}")
	print(f"And the ingredients are:\n")
	for ingredient in ingredients:
		print(ingredient)

make_sandwich("Bread Sandwich", 'bread slices', 'bacon', 'lettuce', 'cheese', 'butter')
make_sandwich("Chocolate Sandwich", 'chocolate bars', 'solidified milk bar', 'wafer', 'candy', 'butter')
make_sandwich("Biscuit Sandwich", 'square Biscuits', 'marshed cookies', 'milk', 'butter')