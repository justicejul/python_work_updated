
# class User:

#     def __init__(self, first_name, last_name, age, hobbies):

#         self.first_name = first_name
#         self.last_name = last_name
#         self.full_name = f"{first_name} {last_name}"
#         self.age = age
#         self.hobbies = hobbies
#         self.login_attempts = 0

#     def describe_user(self):
#         print(f"This is {self.full_name}, he is {self.age} and he loves {self.hobbies}")

#     def greet_user(self):
#         print(f"hwfar {self.first_name}, how're you today.")

#     def increment_login_attempts(self):
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         self.login_attempts = 0


# class Privileges:
#     def __init__(self, *privileges):
#         self.privileges = privileges
    
#     def show_privileges(self, *privileges):
#         for privilege in self.privileges:
#             # return privilege
#             print(privilege)


# class Admin(User):

#     def __init__(self,  first_name, last_name, age, hobbies):

#         super().__init__(first_name, last_name, age, hobbies)
        
#         self.privileges = Privileges()



# user = Admin("Justice", "Julius", 18, "Eating")
# print(user.full_name)
# user.privileges.show_privileges("can add post", "can delete post", "can ban user")




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



# # Write a separate Privileges class. 
# # The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
# # Move the show_privileges() method to this class.
# # Make a Privileges instance as an attribute in the Admin class. 
# # Create a new instance of Admin and use your method to show its privileges.

class Privileges:
    def __init__(self, *privileges):
         self.privileges = privileges

    def show_privileges(self, *privileges):
        for privilege in privileges:
            print(privilege)



class Admin(User):

    def __init__(self,  first_name, last_name, age, hobbies):

        super().__init__(first_name, last_name, age, hobbies)
        
        self.privileges = Privileges()


# User = Admin("Justice", "Julius", 18, "Food")
# User.privileges.show_privileges("can add post", "can delete post", "can ban user")

# I made a bunch of mistakes which i'm going to list out.
# let user=new User({})