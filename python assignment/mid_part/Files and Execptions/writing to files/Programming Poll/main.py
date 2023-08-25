# Write a while loop that asks people why they like programming.
# Each time someone enters a reason, add their reason to a file
# that stores all the responses.
signal = True
while signal:
    name = input("what is your name?: ")
    if name != "":
        answer = input("why do you like programming?: ")
        if answer != "":
            print("Thank you!")

            with open('reasons.txt', 'a') as object_file:
                object_file.write(f"{name}'s reason for liking programming was,\"{answer}\" ")
    reply = input("Do you want to go again?: ")
    if reply.title() == "No":
        break

