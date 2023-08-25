# Write a while loop that prompts users for their name. When
# they enter their name, print a greeting to the screen and add a line recording
# their visit in a file called guest_book.txt. Make sure each entry appears on a
# new line in the file.
star = True
while star:
    answer = input("Do you want to give remarks?:")
    if answer.title() == "No":
        break
    else:
        print("Ok let's go!")

    name = input("What is your name?: ")
    if name != "":
        Report =  f"Hello! {name}, could you please tell me how your visit to our website was?: "
        report = input(Report)
        if report != "":
            with open('VisitRemarks.txt ', 'a') as object_file:
                object_file.write(f"\n{name}'s response was \"{report}\"")
