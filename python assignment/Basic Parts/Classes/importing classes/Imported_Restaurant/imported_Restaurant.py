# Using your latest Restaurant class, store it in a module. 
# Make a separate file that imports Restaurant. 
# Make a Restaurant instance, and call one of Restaurant’s methods 
# to show that the import statement is working properly


class Restaurant:
	"""creating a resturant class"""
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print("Delicious foods!")

	def open_restaurant(self):
		print(f"{self.restaurant_name} is now open!")

	def set_number_served(self, value):
		if value >= self.number_served:
			self.number_served = value
		else:
			print(f"we can't roll back.")
			# number_served = number_served

	def increment_number_served(self, value):
	    if value >= self.number_served:
	    	self.number_served += value
	    else:
	    	print(f"we can't roll back.") 
