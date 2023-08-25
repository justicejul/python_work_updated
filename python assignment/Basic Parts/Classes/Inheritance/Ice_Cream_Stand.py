# An ice cream stand is a specific kind of restaurant. 
# Write a class called IceCreamStand that inherits from the Restaurant class you wrote 
# in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). 
# Either version of the class will work; just pick the one you like better. 
# Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. 
# Create an instance of IceCreamStand, and call this method.

"""Getting the restaurant class i wrote in Exercise 9-4 (page 167). """

class Restaurant:
	"""creating a resturant class"""
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print("Delicious foods!")

	def open_restaurant(self):
		print("We are now open!")

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


class IceCreamStand(Restaurant):

	def __init__(self, *flavors):

		self.flavors = flavors

	def displayFlavors(self):
		print(self.flavors)

myIce_cream = IceCreamStand("Vanila-flavor", "Strawberry-flavor", "Banana-flavor", "Chocolate-flavor")
myIce_cream.displayFlavors()