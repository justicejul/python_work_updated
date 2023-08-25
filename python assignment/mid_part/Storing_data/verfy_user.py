# The final listing for remember_me.py assumes either that the user
# has already entered their username or that the program is running for the first time.

import json
def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
        return username

# We should modify it in case the current user is not the person who last used the program.
# Before printing a welcome back message in greet_user(),
# ask the user if this is the correct username.
# If it’s not, call get_new_username() to get the correct username.

def greet_user():
    """Greet the user by name."""
    while True:
        username = get_stored_username()
        if username:
            answer = input(f"Is this your username:{username}?\n Please answer with Yes or No : ")
            if answer.title() == "Yes":
                print(f"Welcome back, {username}!")
                break
            elif answer.title() == "No":
                username = get_new_username()
                print(f"We'll remember you when you come back, {username}!")
                break
            else:
                print("That is not a valid answer!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
            break


greet_user()
