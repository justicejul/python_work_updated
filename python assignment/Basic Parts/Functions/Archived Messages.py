# Start with your work from Exercise 8-10. Call the function send_messages() with a 
# copy of the list of messages. After calling the function, print both of your lists 
# to show that the original list has retained its messages.


# def send_messages(messages, new_list):
# 	while messages:
# 		message = messages.pop()
# 		print (message) 
# 		new_list.append(message)


def send_messages(messages, new_list):
	while messages:
		message = messages.pop()
		print (message) 
		new_list.append(message)

text_messages = ["hey, how're you", "what's up", "hello", "i'm ok", "i love u"]
sent_messages = []

send_messages(text_messages[:], sent_messages)
print(sent_messages)
print(text_messages)