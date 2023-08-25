# Start with your program from Exercise 8-7. 
# Write a whileloop that allows users to enter an album’s artist and title. 
# Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
# Be sure to include a quit value in the while loop.

# def make_album(artist_name, album_title):
# 	music = {}
# 	music[artist_name] = album_title
# 	return music



# while True:
# 	print("\nTell us your most favourite artist and one of his albums")

# 	artist = input("\nwho is your fav artist? ")
# 	if artist == "quit":
# 		break

# 	Name_of_album = input("\nMention one of his albums ")
# 	if Name_of_album == "quit":
# 		break

#     Repeat = "\nShould we ask the next person? "
#     Repeat += "Yes/No"

#     if Repeat == "no":
#     	break

#     print(make_album(artist, Name_of_album))


def make_album(artist_name, album_title):
    music = {}
    music[artist_name] = album_title
    return music



while True:
    print("\nTell us your most favourite artist and one of his albums")
    artist = input("\nwho is your fav artist? ")
    if artist == "quit":
        break

        
    Name_of_album = input("\nMention one of his albums ")
    if Name_of_album == "quit":
        break

    print(make_album(artist, Name_of_album))    
        
    repeat = "\nShould we ask the next person? "
    repeat += "Yes/No"
    Repeat= input(repeat)
    
    if Repeat == "no":
        break