# Start with your work from Exercise 9-8 (page 173). 
# Store the classes User, Privileges, and Admin in one module. 
# Create a separate file, make an Admin instance, and call show_privileges() 
# to show that everything is working correctly.

from Stored_classes import Admin as ad
from Stored_classes import User as us

# User = str(input('input your name \n'))
User = ad("Justice", "Julius", "18", "Eating")
User.privileges.show_privileges("can add post", "can delete post", "can ban user")