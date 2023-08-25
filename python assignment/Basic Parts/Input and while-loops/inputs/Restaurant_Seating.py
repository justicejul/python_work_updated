# Write a program that asks the user how many people 
# are in their dinner group. If the answer is more than eight, 
# print a message saying they’ll have to wait for a table. 
# Otherwise, report that their table is ready

dinner_grp_No = input("How many people are in the dinner group?")
if dinner_grp_No > 8:
	print("Sorry, you'll have to wait for another table")
else:
	print("Your table is ready")