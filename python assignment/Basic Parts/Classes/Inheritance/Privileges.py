# Write a separate Privileges class. 
# The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
# Move the show_privileges() method to this class.
# Make a Privileges instance as an attribute in the Admin class. 
# Create a new instance of Admin and use your method to show its privileges.

# class Privileges:

#     def __init__(self, privileges=None):
#         if privileges == None:
#             self.privileges = []
#         else:
#             self.privileges = privileges

#         # self.privileges = privileges = []

#         def show_privileges(self):
#             for privilege in self.privileges:
#                 print(privilege) 

class Privileges:
    def __init__(self, *privileges):

        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege) 


print(Privileges("ffhhhhgg", "jgjjdfdjj", "yu,znmkl"))
print(Privileges("ffhhhhgg", "jgjjdfdjj", "yu,znmkl"))