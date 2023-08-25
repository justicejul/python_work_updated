# Write a function called city_country() that takes in the name of a city and its country. 
# The function should return a string formatted like this: "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(city, country):
	message = f'"{city}, {country}"'
	return message

print(city_country("abuja", "Nigeria"))
print(city_country("accra", "Ghana"))
print(city_country("johanesseburg", "South-Africa"))