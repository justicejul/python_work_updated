# 6-8. Pets: Make several dictionaries, where each dictionary represents  a different pet. 
#In each dictionary, include the kind of animal and the owner’s name. 
#Store these dictionaries in a list called pets. 
#Next, loop through your list and as you do, print everything you know about each pet.

Bingo = {
	'Name of pet' :'Dog', 
	'Name of owner' : 'Mr Henry',
	'Type of animal' : 'Mammal',
	'Life Span' : '13 years',

}

Pussy = {
	'Name of pet' :'Cat', 
	'Name of owner' : 'Miss Virginia',
	'Type of animal' : 'Mammal',
	'Life Span' : '18 years',
}

Cock = {
    'Name of pet': 'Fowl',
	'Name of owner': 'Mr Dickson',
	'Type of animal' : 'Non mammal',
	'Life Span' : '10 years',
}

Ben = {
	'Name of pet':'Python', 
	'Name of owner': 'Mr Guido von rossum',
	'Type of animal' : 'Non mammal',
	'Life Span' : '30 years',
}

Squrry = {
	'Name of pet' : 'Squirrel',
	'Name of owner' : 'John',
	'Type of animal' : 'Mammal',
	'Life Span' : '10 years',
}

Kami = {
	'Name of pet' : 'Eagle',
	'Name of owner' : 'Justice',
	'Type of animal' : 'Non mammal',
	'Life Span' : '50 years',
}


Pets = [Bingo, Pussy, Cock, Ben, Squrry, Kami]
vowels = ['A','E','I','O','U']
for pet in Pets:
	if f"{pet['Name of pet'][0]}" in vowels:
		print(f"This is an {pet['Name of pet']}")
	elif f"{pet['Name of pet'][0]}" not in vowels:
		print(f"This is a {pet['Name of pet']}")
        print(f"The owner of the pet is {pet['Name of owner']}")
        print(f"This animal is a {pet['Type of animal']}")
        print(f"They have a Life Span of {pet['Life Span']}\n")
    