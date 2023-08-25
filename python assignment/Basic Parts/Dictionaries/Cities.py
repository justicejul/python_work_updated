# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
# Create a dictionary of information about each city and include the country that the city is in, its 
# approximate population, and one fact about that city. The keys for each city’s dictionary should be something 
# like country, population, and fact. Print the name of each city and all of the information you have stored about it.

Cities = {
	'baltimore' : {
    
    'Country' : 'America',
    'Population' : 576_498,
    'Fact' : 'the first umbrella factory in the United States was established in Baltimore in 1828.',
	},

	'puebla' : {
    
    'Country' : 'Mexico',
    'Population' : 1_692_181,
    'Fact' : 'puebla is where you will find Mescoamerica\'s largest ancient city.',
	},

    'uyo' : {
    
    'Country' : 'Nigeria',
    'Population' :  436_606,
    'Fact' : 'it is the capital of of the state that is one of Nigeria\'s 36 states with a population of over 5 million people and more than 10 million people in diaspora.',
	}
}


for city,infos in Cities.items():
	print(f"\nThis is {city.title()}, fun fact is that, {infos['Fact']}")
	print(f"And it has a population of {infos['Population']}")
	