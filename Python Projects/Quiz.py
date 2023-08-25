# prompt = "Hello, i'd like for you to test my game."
# prompt += "\nBefore we proceed, Your name please: "

# name = ""

# while name == "":
# 	name = input(prompt)
# 	print(name)

# print(f"hwfar {name}")



# if name == "":
# 	print("Sorry, but you cannot proceed without inputting your name")



# while message != 'quit':
#  message = input(prompt)
#  print(message)


 


# prompt = "Hello, i'd like for you to test my game."
# prompt += "\nBefore we proceed, Your name please:  "

# PLayer_name = ""

# while Player_name == "":
#     Player_name = input(prompt)

# print(f"\n{Player_name.title()} you may now proceed")

print(f"This question has three sections.\nThe first part being the easy part.\nThe second is going to be harder than the first.\nAnd the third being harder than the second.")









real_owner = "Sanusi Ismaila"

while True:
    owner = input("Who founded Colab?: ")

    if owner.title() == real_owner or owner.title() in real_owner:
        print("You're correct!")
        break
    else:
        print("Wrong! Try again.")

    Real_Year = "2017"

    Year = input("When was Colab founded?: ")

	if Year == Real_Year:
		
		print("You're Correct!")
	else:
		print("Wrong!, try again")




# flag = True
# while flag:
# 	Real_Owner = "Sanusi Ismaila"
# 	Owner = input("Who founded Colab?: ")
# 	if Owner != Real_Owner or  Owner not in Real_Owner:
# 		print("You're wrong!")
# 	else:
# 		print("Wrong!, try again.")
# 		print(Owner)






# flag = True
# while flag:
# 	Real_Owner = "Sanusi Ismaila"
# 	Owner = input("Who founded Colab?: ")
# 	if Owner == Real_Owner or  Owner in Real_Owner:
# 		print("You're Correct!")
# 	else:
# 		print("Wrong!, try again.")
# 		print(Owner)

# Real_Year = "2017"
# Year = input("When was Colab founded?: ")
# if Year == Real_Year:
# 	print("You're Correct!")
# else:
# 	print("Wrong!, try again")
# 	print(Year)

# interns = ["Tumi", "Isaac", "Solomon", "Aji", "segun", "Feranmi", "Abdulsamad", "Blessing", "Motunrayo", "Opeyemi", "Barakat", "Mildred", "Hamdallat", "Wisdom", "Bello", "Emmanuel" ]
# answer = input("Name five interns that you in Colab: ")

# if answer != interns:
# 	print("Wrong!, try again")
# 	print(answer)
# else:
# 	print("You're Correct!")




# flag = True
# while flag:
#     Real_Owner = "Sanusi Ismaila" 
#     Owner.title() = input("Who founded Colab?: ")
#     if Owner.title() == Real_Owner or  Owner.title() in Real_Owner:
#         print("You're Correct!")
#         break
#     else:
#         print("Wrong!, try again.")
        
# while flag:
#     Real_Year = "2017"
#     Year = input("When was Colab founded?: ")
#     if Year == Real_Year:
#         print("You're Correct!")
#         break
#     else:
#         print("Wrong!, try again")
        
# while flag:
#     Real_governor = "Nasir el-rufai"
#     Governor.title() = input("Who is the Current Governor of Kaduna State?")
#     if Governor == Real_Year:
#         print("You're Correct!")
#         break
#     else:
#         print("Wrong!, try again")
        



flag = True
while flag:
    Real_Owner = "Sanusi Ismaila"
    owner = input("Who founded Colab?: ")
    if owner.title() == Real_Owner or  owner.title() in Real_Owner:
        print("You're Correct!")
        break
    else:
        print("Wrong!, try again.")
        
while flag:
    Real_Year = "2017"
    Year = input("When was Colab founded?: ")
    if Year == Real_Year:
        print("You're Correct!")
        break
    else:
        print("Wrong!, try again")
        
while flag:
    Real_governor = "Nasir el-rufai"
    Governor = input("Who is the Current Governor of Kaduna State?")
    if Governor.title() == Real_Year:
        print("You're Correct!")
        break
    else:
        print("Wrong!, try again")
        
while flag:
    Better_language = ["None", "No one", "Depends", "It depends"]
    better_langguage = input("Between python and javascript, which is better?")
    if better_langguage.title() in Better_language:
        print("You're correct!")
        break
    else:
        print("Wrong!, try again")

while flag:
    Bald_guy = "Pablo"
    bald_guy = input("Between Pablo and Sanusi who is more bald ?")
    if bald_guy.title() == Bald_guy:
        print("Gooooood!, you get correct eye.")
        break
    else:
        print("Wtf!, are you blind? \n Abeg try again! ")

while flag:
    theSinger = "Musa Keys"
    the_singer = input("Who was featured in the song \"unavailable\" by Davido")
    if the_singer.title() == theSinger:
        print("You're correct!")
        break
    elif the_singer.title() == "Musa" or the_singer.title() == "Keys":
        print("please print the full name.")
    else:
        print("Wrong!, try again")
    
    