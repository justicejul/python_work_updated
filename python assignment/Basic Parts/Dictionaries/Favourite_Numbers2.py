# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99) 
# so each person can have more than one favorite number. Then print each 
# person’s name along with their favorite numbers

numbers = {
	'justice': [8, 18],
	'blessing': [17, 5],
	'usman': [19, 35],
	'juliet' : [3, 11],
	'Pablo' : [16,7],
     }

for names, nums in numbers.items():
 	print(f"\n{names.title()} favourite numbers are:")
 	for num in nums:
 		print(f"\t{num}")
