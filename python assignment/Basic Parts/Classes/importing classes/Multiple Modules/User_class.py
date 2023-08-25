
class User:

    def __init__(self, first_name, last_name, age, hobbies):

        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        self.age = age
        self.hobbies = hobbies
        self.login_attempts = 0

    def describe_user(self):
        print(f"This is {self.full_name}, he is {self.age} and he loves {self.hobbies}")

    def greet_user(self):
        print(f"hwfar {self.first_name}, how're you today.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
