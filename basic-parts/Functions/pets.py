
def describe_pet(animal_type, pet_name):

     """Display information about a pet."""
     print(f"\nI have a {animal_type}.")
     print(f"My {animal_type}'s name is {pet_name.title()}.") 

escribe_pet('Hamster', 'harry')

#Multiple function calls

def describe_pet(animal_type, pet_name):

     """Display information about a pet."""
     print(f"\nI have a {animal_type}.")
     print(f"My {animal_type}'s name is {pet_name.title()}.") 

describe_pet('Dog', 'Bingo')
describe_pet('Hamster', 'harry')
describe_pet('Dragon', 'willie')

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')