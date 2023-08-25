from Admin__privilege_classes import Admin as ad
from Admin__privilege_classes import User as us

# User = str(input('input your name \n'))
User1 = ad("Justice", "Julius", "18", "Eating")
User1.privileges.show_privileges("can add post", "can delete post", "can ban user")
User2 = ad("Hamdyy", "Yemi", "21", "Eating")
User2.privileges.show_privileges("\nEdit profile", "Block friends", "Change password" )
