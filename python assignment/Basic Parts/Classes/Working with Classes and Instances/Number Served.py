# Start with your program from Exercise 9-1 (page 162). 
# Add an attribute called number_served with a default value of 0. 
# Create an instance called restaurant from this class. 
# Print the number of customers the restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of customers that have been served. 
# Call this method with a new number and print the value again.
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
# Call this method with any number you like that could represent how many customers were served in, say, a day of business.


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


restaurant = Restaurant("Colab_foods", "Native dishes")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# print("\n")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

print(f"We, {restaurant.restaurant_name} serve the best {restaurant.cuisine_type}")
print(f"we have served {restaurant.number_served} customers today")

 ######
 ######

restaurant.number_served = 8

print(f"\nWe, {restaurant.restaurant_name} serve the best {restaurant.cuisine_type}")
print(f"we have served {restaurant.number_served} customers today")

 #####
 #####

restaurant.set_number_served(30)

print(f"\nWe, {restaurant.restaurant_name} serve the best {restaurant.cuisine_type}")
print(f"we have served {restaurant.number_served} customers today")


#####
#####

restaurant.increment_number_served(40)

print(f"\nWe, {restaurant.restaurant_name} serve the best {restaurant.cuisine_type}")
print(f"we have served {restaurant.number_served} customers today")

