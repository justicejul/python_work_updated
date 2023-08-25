# def count_words(filename):
#     """Count the approximate number of words in a file."""
#     try:
#         with open(filename, encoding='utf-8') as f:
#             contents = f.read()
#     except FileNotFoundError:
#         print(f"Sorry, the file {filename} does not exist.")
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file {filename} has about {num_words} words.")
#
#
# filename = 'alice.txt'
# count_words(filename)

# filename = 'alice.txt'
# try:
#     with open(filename, encoding='utf-8') as f:
#         contents = f.read()   
# except FileNotFoundError:
#     print(f"Sorry, the file {filename} does not exist.")
# else:
#     # Count the approximate number of words in the file
#     words = contents.split()
#     num_words = len(words)
#     print(f"The file {filename} has about {num_words} words.")

# TURNING OUR TEXT FILE OPENER TO A FUNCTION TO EASILY CHECK MULTIPLE FILES
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

# USING THE PASS STATEMENT IN EXCEPTIONS
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)