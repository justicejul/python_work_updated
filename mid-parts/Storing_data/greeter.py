import json

filename = 'username.json'

with open(filename, 'r') as fB:
    Username = json.load(fB)
    print(f"We remember you{Username}!")