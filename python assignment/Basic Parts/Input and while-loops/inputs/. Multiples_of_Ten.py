# Ask the user for a number, and then report whether the 
# number is a multiple of 10 or not..


number = input("Choose a number? ")
number = int(number)

if number % 10 == 0:
	print("This number is divisible by 10")
else:
	print("This numberis not divisible by 10")