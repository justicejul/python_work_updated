text_file = 'C:\\Users\\Lenovo\\Desktop\\message1.txt'

with open(text_file, 'w') as object_file:
	content = object_file.write("i'm overwriting this ")

with open(text_file, 'a') as object_file:
	content = object_file.write("\nbichhhh, fuck off!")	
	