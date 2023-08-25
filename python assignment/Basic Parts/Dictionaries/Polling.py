# Use the code in favorite_languages.py (page 97).

# •	 Make a list of people who should take the favorite languages poll. Include 
#some names that are already in the dictionary and some that are not. 

# •	 Loop through the list of people who should take the poll. If they have already 
#taken the poll, print a message thanking them for responding. 
# If they have not yet taken the poll, print a message inviting them to take the poll.

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 'tobi': 'javascript',
 'rico': 'c++',
 'polycarp': 'c#',

 }


names = ['pablo', 'tobi', 'purest', 'rico', 'sarah', 'justice', 'bolaji']

for name in names:
	if name in favorite_languages:
		print(f"{name}, thank you for having taken the poll\n")
	else:
		print(f"{name}, please kindly come and take the poll\n")
