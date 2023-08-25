# Make a list called sandwich_orders and fill it with the names of various sandwiches. 
# Then make an empty list called finished_sandwiches. Loop through the list of sandwich 
# orders and print a message for each order, such as I made your tuna sandwich. As each 
# sandwich is made, move it to the list of finished sandwiches. After all the sandwiches 
# have been made, print a message listing each sandwich that was made.


sandwich_orders = ["panini", "cheese-steak", "chicken ", "vegetable", "ham", "cuban", "meatball", "pinwheel", "pastrami", "ice-cream", "muffuletta"]
finished_sandwiches = []

while sandwich_orders:
	current_sandwiches = sandwich_orders.pop()
	
	print(f"\ni made your {current_sandwiches} sandwich")
	
	finished_sandwiches.append(current_sandwiches)
print("\n\n\n")

for finished_sandwich in finished_sandwiches:

	print(f"\nCome and get your {finished_sandwich} sandwich")