# Make a class Die with one attribute called sides, which has a default 
# value of 6. Write a method called roll_die() that prints a random number 
# between 1 and the number of sides the die has. Make a 6-sided die and roll it 
# 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Die:

	def __init__(self, sides=6):
         
         self.sides = sides
		

	def roll_die(self):
		result = randint(1, self.sides)
		return result

six_sided_die = Die()
for i in range(10):
	print(six_sided_die.roll_die())

print("\n")

ten_sided_die = Die(10)
for x in range(20):
	print(ten_sided_die.roll_die())