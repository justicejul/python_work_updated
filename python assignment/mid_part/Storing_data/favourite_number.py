# Write a program that prompts for the user’s favorite number.
# Use json.dump() to store this number in a file.
# Write a separate program that reads in this value and prints the message,
# “I know your favorite number! It’s _____.”

import json

Fave_number = input("Can you tell me what your favourite is ?: ")
filename = 'faveNumber.json'
with open(filename, "w") as f:
    json.dump(Fave_number, f)


with open("faveNumber.json", 'r') as f:
    json.load(f)
    print(f"I know your favorite number! It's {Fave_number}.")

