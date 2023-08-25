# Combine the two programs from Exercise into one file.
# If the number is already stored, report the favorite number to the user.
# If not, prompt for the user’s favorite number and store it in a file.
# Run the program twice to see that it works.
import json
filename = "faveNumber.json"
try:
    with open(filename, 'r') as f:
        Fave_number = json.load(f)
except FileNotFoundError:
    Fave_number = input("Can you tell me what your favourite is ?: ")
    with open(filename, "w") as f:
        json.dump(Fave_number, f)
else:
    print(f"I know your favorite number! It's {Fave_number}.")







