# Add an attribute called login_attempts to your Userclass from Exercise 9-3 (page 162). 
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts() several times. 
# Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
# Print login_attempts again to make sure it was reset to 0.

class User:
	def __init__(self, first_name, last_name, age, hobbies):

		self.first_name = first_name
		self.last_name = last_name
		self.full_name = f"{first_name} {last_name}"
		self.age = age
		self.hobbies = hobbies
		self.login_attempts = 0

	def describe_user(self):
		print(f"This is {full_name}, he is {age} and he loves {hobbies}")

	def greet_user(self):
		print(f"hwfar {first_name}, how're you today.")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

    

user_1 = User("Justice", "Julius", 18, "Food")

user_1.increment_login_attempts()
print(user_1.login_attempts)

user_1.increment_login_attempts()
print(user_1.login_attempts)

user_1.increment_login_attempts()
print(user_1.login_attempts)

user_1.increment_login_attempts()
print(user_1.login_attempts)


user_1.reset_login_attempts()
print(user_1.login_attempts)


print(user_1.login_attempts)


# user_2 = User("David", "Johnson", 24, "Swimming")
# user_3 = User("Naomi", "Usman", 28, "Carrying babies")
# user_4 = User("Ele", "Usman", 24, 'Saying, "it\'ll be fine "')
