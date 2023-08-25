# Start with a copy of your program from Exercise 8-9. 
# Write a function called send_messages() 
# that prints each text message and 
# moves each message to a new list called sent_messages as it’s printed. After 
# calling the function, print both of your lists to make sure the messages were 
# moved correctly.

# def show_messages(messages):
#     for message in messages:
#         print(message)


# text_messages = ["hey, how're you", "what's up", "hello", "i'm ok", "i love u"]
# show_messages(text_messages)



def send_messages(messages, new_list):
	while messages:
		message = messages.pop()
		print (message) 
		new_list.append(message)

text_messages = ["hey, how're you", "what's up", "hello", "i'm ok", "i love u"]
sent_messages = []

send_messages(text_messages, sent_messages)
print(sent_messages)