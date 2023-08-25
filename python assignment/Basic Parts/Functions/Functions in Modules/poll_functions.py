def identity(name, age, height, location, work, **profile):
	"""Creating a function that stores someone's data in adictionary"""
	profile["Name"] = name.title()
	profile["Age"] = age
	profile["Height"] = height.title()
	profile["Location"] = location.title()
	profile["Work"] = work.title()
	return profile
