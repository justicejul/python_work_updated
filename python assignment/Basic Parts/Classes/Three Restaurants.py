# Start with your class from Exercise 9-1. Create three different instances from the class, 
# and call describe_restaurant() for each instance.


class Restaurant:
	"""creating a resturant class"""
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print("Delicious foods!")

	def open_restaurant(self):
		print("We are now open!")

# from Restaurant import Restaurant as rs 

rest_1 = Restaurant("MJ_confectionaries", "Native Nigerian foods")
rest_2 = Restaurant("Colab_foods", "Best nigerian dishes")
rest_3 = Restaurant("Ritis", "Modern Nigerian Dishies")
print(rest_1.restaurant_name)
print(rest_2.restaurant_name)
print(rest_3.restaurant_name)

rest_1.describe_restaurant()
rest_2.describe_restaurant()
rest_3.describe_restaurant()