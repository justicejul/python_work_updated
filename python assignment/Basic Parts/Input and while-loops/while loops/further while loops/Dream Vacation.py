# Write a program that polls users about their dream vacation. 
# Write a prompt similar to If you could visit one place in the world, where 
# would you go? Include a block of code that prints the results of the poll.

polls = {}

flag = True
while flag:
    name = input("\nWhat is your name?")
    Dream_place = input("If you could visit one place in the world, where would you go?\n")
    
    polls[name] = Dream_place

    ask_again = input("\nShould we ask the next person?")

    if ask_again == "no":
        flag = False

for name, Dream_place in polls.items():
    print("\n.......Results........")
    print(f"\n{name} would like to visit {Dream_place}")