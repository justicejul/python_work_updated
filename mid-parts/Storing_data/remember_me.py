import json

Username = input("what is your name? :")

filename = 'username.json'

with open(filename, 'w') as fB:
    json.dump(Username, fB)
    print(f"We'll remember you when you come back,{Username}")
