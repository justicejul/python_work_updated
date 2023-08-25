# Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored 
# in a user profile. Make a method called describe_user() that prints a summary 
# of the user’s information. Make another method called greet_user() that prints 
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods 
# for each user.

class User:
	def __init__(self, first_name, last_name, age, hobbies):

		self.first_name = first_name
		self.last_name = last_name
		self.full_name = f"{first_name} {last_name}"
		self.age = age
		self.hobbies = hobbies

	def describe_user(self):
		print(f"This is {full_name}, he is {age} and he loves {hobbies}")
	def greet_user(self):
		print(f"hwfar {first_name}, how're you today.")


user_1 = User("Justice", "Julius", 18, "Food")
user_2 = User("David", "Johnson", 24, "Swimming")
user_3 = User("Naomi", "Usman", 28, "Carrying babies")
user_4 = User("Ele", "Usman", 24, 'Saying, "it\'ll be fine "')


user_1.describe_user()
user_2.describe_user()
user_3.describe_user()
user_4.describe_user()