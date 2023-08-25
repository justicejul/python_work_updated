# An administrator is a special kind of user. Write a class called 
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) 
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list 
# of strings like "can add post", "can delete post", "can ban user", and so on. 
# Write a method called show_privileges() that lists the administrator’s set of 
# privileges. Create an instance of Admin, and call your method.



# class User:
#     def __init__(self, first_name, last_name, age, hobbies):

#         self.first_name = first_name
#         self.last_name = last_name
#         self.full_name = f"{first_name} {last_name}"
#         self.age = age
#         self.hobbies = hobbies
#         self.login_attempts = 0

#     def describe_user(self):
#         print(f"This is {full_name}, he is {age} and he loves {hobbies}")

#     def greet_user(self):
#         print(f"hwfar {first_name}, how're you today.")

#     def increment_login_attempts(self):
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         self.login_attempts = 0




# class Admin(User):

#     def __init__(self, first_name, last_name, age, hobbies, *privileges):

#         super().__init__(first_name, last_name, age, hobbies)


















# ///////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////




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


class Privilege:

    def __init__(self, *privileges):

        self.privileges = privileges

    def show_privileges(self, *privileges):
        for privilege in self.privileges:
            print(privilege)

# thePrivileges = Privilege("can add post", "can delete post", "can ban user")
# thePrivileges.show_privileges()

class Admin(User):

    def __init__(self,  first_name, last_name, age, hobbies):

        super().__init__(first_name, last_name, age, hobbies)

        self.privileges = Privilege()


user_1 = Admin("Justice", "Julius", 18, "Eating").show_privileges("can add post", "can delete post", "can ban user")
# user_1 = Admin.show_privileges("can add post", "can delete post", "can ban user")


        
    #     self.privileges = privileges

    # def show_privileges(self):
    #     for privilege in self.privileges:
    #         print(privilege)


# User = Admin("Justice", "Julius", 18, "Food")
# User.privileges.show_privileges("can add post", "can delete post", "can ban user")



# ?????????????????????????????????????????????????????????????????????????????????????????????????
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# # Write a separate Privileges class. 
# # The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
# # Move the show_privileges() method to this class.
# # Make a Privileges instance as an attribute in the Admin class. 
# # Create a new instance of Admin and use your method to show its privileges.


# class User:

#     def __init__(self, first_name, last_name, age, hobbies):

#         self.first_name = first_name
#         self.last_name = last_name
#         self.full_name = f"{first_name} {last_name}"
#         self.age = age
#         self.hobbies = hobbies
#         self.login_attempts = 0

#     def describe_user(self):
#         print(f"This is {full_name}, he is {age} and he loves {hobbies}")

#     def greet_user(self):
#         print(f"hwfar {first_name}, how're you today.")

#     def increment_login_attempts(self):
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         self.login_attempts = 0



# # # Write a separate Privileges class. 
# # # The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
# # # Move the show_privileges() method to this class.
# # # Make a Privileges instance as an attribute in the Admin class. 
# # # Create a new instance of Admin and use your method to show its privileges.

# class Privileges:
#     def __init__(self, *privileges):
#          self.privileges = privileges

#     def show_privileges(self, *privileges):
#         for privilege in self.privileges:
#             print(privilege)



# class Admin(User):

#     def __init__(self,  first_name, last_name, age, hobbies):

#         # super().__init__(self, first_name, last_name, age, hobbies)
        
#         self.privileges = Privileges()


# User = Admin("Justice", "Julius", 18, "Food")
# User.privileges.show_privileges("can add post", "can delete post", "can ban user")









# /////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////




# # Write a separate Privileges class. 
# # The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
# # Move the show_privileges() method to this class.
# # Make a Privileges instance as an attribute in the Admin class. 
# # Create a new instance of Admin and use your method to show its privileges.




# class Privileges:

#     def __init__(self, *privileges):

#         self.privileges = privileges


#     def show_privileges(self):
#         for privilege in self.privileges:
#             print(privilege) 


# class Admin(User):

#     def __init__(self,  first_name, last_name, age, hobbies, *privileges):

#         # super().__init__(self, first_name, last_name, age, hobbies)
        
#         self.privileges = privileges

#     def show_privileges(self):
#         for privilege in self.privileges:
#             print(privilege)


# User = Admin("Justice", "Julius", 18, "Food", "can add post", "can delete post", "can ban user")
# User.show_privileges()
# # User.show_privileges()







# #                   #Question:

# # # Q1 - After getting the __init__() method of the parent class, along with the contents inside (the parameter values), 
# # # do we need to still need to copy the parent parameter values into our child class. 

# # # Q2 - when putting in our arguments and the position - which side, they are to be putted, do we consider the parent 
# # # parameter to be the first or child parameters values to be first. 









# class User:

#     def __init__(self, first_name, last_name, age, hobbies):

#         self.first_name = first_name
#         self.last_name = last_name
#         self.full_name = f"{first_name} {last_name}"
#         self.age = age
#         self.hobbies = hobbies
#         self.login_attempts = 0

#     def describe_user(self):
#         print(f"This is {full_name}, he is {age} and he loves {hobbies}")

#     def greet_user(self):
#         print(f"hwfar {first_name}, how're you today.")

#     def increment_login_attempts(self):
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         self.login_attempts = 0





# # Write a separate Privileges class. 
# # The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
# # Move the show_privileges() method to this class.
# # Make a Privileges instance as an attribute in the Admin class. 
# # Create a new instance of Admin and use your method to show its privileges.







# class Privileges:

#     def __init__(self, *privilegess):

#         self.privilegess = privilegess


#     def show_privileges(self):
#         for privileges in self.privilegess:
#             return privileges 


# class Admin(User):

#     def __init__(self,  first_name, last_name, age, hobbies, *privilegess):

#         # super().__init__(self, first_name, last_name, age, hobbies)
        
#         self.privileges = Privileges()

#     # def show_privileges(self):
#     #     for privilege in self.privileges:
#     #         print(privilege)


# User = Admin("Justice", "Julius", 18, "Food", "can add post", "can delete post", "can ban user")
# User.privileges.show_privileges()
# # User.show_privileges()
