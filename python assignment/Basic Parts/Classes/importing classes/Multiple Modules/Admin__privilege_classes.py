from User_class import User

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
