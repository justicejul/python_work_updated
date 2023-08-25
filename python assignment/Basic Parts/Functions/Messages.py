# Messages: Make a list containing a series of short text messages. Pass the 
# list to a function called show_messages(), which prints each text message.

def show_messages(messages):
    for message in messages:
        print(message)


text_messages = ["hey, how're you", "what's up", "hello", "i'm ok", "i love u"]
show_messages(text_messages)