# You can use a loop to see how hard it might be to win the kind of lottery you just modeled. 
# Make a list or tuple called my_ticket. 
# Write a loop that keeps pulling numbers until your ticket wins. Print a message 
# reporting how many times the loop had to run to give you a winning ticket.

from random import choice 


lottery_list = ["J", 3, 5, "H", 1, "O", 45, 18, 19, 13, "D", 81,"E", 8, 25]
# Lucky_winner = ch(lottery_list)


my_ticket = "J"

# flag = True

# while flag:
# 	if ch(lottery_list) != my_ticket:
# 		flag = False
# 	else:
# 		print(f"{my_ticket} won the lottery today!")
# 	counter += 1

counter = 0
while my_ticket != choice(lottery_list):
	counter += 1
print(f"{my_ticket} won the lottery today!")
print(f"And i had to draw the rawffel {counter} times")



# while True:
# 	counter = 0
# 	if choice(lottery_list) == my_ticket:
# 		print(f"{my_ticket} won the lottery today!")
# 		print(f"i had to pick the rawffel {counter} times before i got it")
# 		break
# 	else:
# 		continue

# 	counter += 1
	
	



	# if Lucky_winner != my_ticket:
	# 	Lucky_winner = ch(lottery_list)
	# else:
	# 	print(f"{my_ticket} won the lottery today!")

	# counter =+ 1

	# continue

