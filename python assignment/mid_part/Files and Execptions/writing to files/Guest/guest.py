names = input("What is Your full name please?: ")


filename = 'guest.txt'
with open(filename, 'w') as object_file:
    object_file.write(names)
    
    