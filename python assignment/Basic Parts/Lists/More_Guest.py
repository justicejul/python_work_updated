names = ['justice', 'pelumi', 'pablo']
print("Okay at first there wasn't enough space, but now \nspace have created. So we'll be inviting more people")
names.insert(0, 'judith')
print(names)
names.insert(5, 'hajirah')
print(names)
names.insert(3, 'fuckson')
print(names)


print(f"\n{names[0].title()} you have beeen invited to the burial of Mr pablo.")
print(f"Dear {names[1].title()}, your father is dead, come for the celebration on monday.")
print(f"{names[2].title()}, we invite you to the burial of our brother.")
print(f"Mr {names[3].title()} you have also been invited.")
print(f"Dear {names[4].title()}, this an invitation for a burial.")
print(f"{names[5].title()}, you're invited to the burial of our nigga.")
 
print(names)

print("\nSorry everybody, just found out that i can only invite \ntwo people, sorry again for the dissapointment")

third_person = names.pop(2)  
print(f"{third_person.title()}, sorry your invitation has been refuted")
fourth_person = names.pop(3) 
print(f"{fourth_person.title()}, sorry your invitation has also been refuted")
fifth_person = names.pop(4) 
print(f"{third_person.title()}, sorry, you too, your invitation has also been refuted")
sixth_person = names.pop(5) 
print(f"{third_person.title()}, sorry your invitation has  also been refuted")








