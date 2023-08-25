# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99). 
# Make two new dictionaries representing different people, and store all three 
# dictionaries in a list called people. Loop through your list of people. As you 
# loop through the list, print everything you know about each person.

Kaminari = {}

Kaminari['First_name'] = 'Justice'
Kaminari['Last_name'] = 'Julius'
Kaminari['Age'] = 17
Kaminari['City'] = 'Kaduna'
Kaminari['Likes'] = 'Boobs'
Kaminari['Food'] = 'Noodles, Fried yam, Fried potatoes, everything mixed'
Kaminari['Fav_color'] = 'Sky blue'


B_J =  {}

B_J['First_name'] = 'Bolaji'
B_J['Last_name'] = 'Oladapo'
B_J['Age'] = 23
B_J['City'] = 'Kaduna'
B_J['Likes'] = 'BJ :)'
B_J['Food'] = 'Noodles'
B_J['Fav_color'] = 'Pink'


Pablo =  {}

Pablo['First_name'] = 'Peter'
Pablo['Last_name'] = 'Okwugoku'
Pablo['Age'] = 33
Pablo['City'] = 'Lagos'
Pablo['Likes'] = 'Everything'
Pablo['Food'] = 'Fried yam'
Pablo['Fav_color'] = 'Green'	 

people = [Kaminari, B_J, Pablo]

for person in people:
	full_name = f"{person['First_name']} {person['Last_name']}"
	print(f"Full name: {full_name}")
	print(f"Age: {person['Age']}")
	print(f"City: {person['City']}")
	print(f"Likes: {person['Likes']}")
	print(f"Food: {person['Food']}")
	print(f"Favourite Food: {person['Fav_color']}\n")