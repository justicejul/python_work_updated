# Make a list or tuple containing a series of 10 numbers and five letters. 
# Randomly select four numbers or letters from the list and print a 
# message saying that any ticket matching these four numbers or letters 
# wins a prize.

from random import choice as ch

lottery_list = ["J", 3, 5, "H", 1, "O", 45, 18, 19, 13, "D", 81,"E", 8, 25]
Lucky_winner = ch(lottery_list)

winner1 = ch(lottery_list)
winner2 = ch(lottery_list)
winner3 = ch(lottery_list)
winner4 = ch(lottery_list)

def list_maker(*winners):
	return winners
	

winners = list_maker(winner1, winner2, winner3, winner4, )
# print(winners)

if Lucky_winner in winners:
	print(f"Number {Lucky_winner}, congrats you're a winner")
else:
	print("Try again next year, sorry!")




















# winners = [25, 5, 19, 18]

# for x in winners:
# 	if x == Lucky_winner:
# 		print(f"congratulations {x}, yo'ure a winner")




# if Lucky_winner in winners:
# 	print(f"congratulations, number {winners} you are part of the few selected!")

# counter = 0
# while 19 not in winners:
# 	break
# 	counter += 1
# else:
# 	print(f"congratulations, number {Lucky_winner} you win the prize!")


# print(f"if your tag matches this value: {Lucky_winner}, you are the winner of the lottery!.")