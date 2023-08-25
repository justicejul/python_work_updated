# Visit Project Gutenberg (https://gutenberg.org/ ) and find a few texts you’d
# like to analyze. Download the text files for these works, or copy the raw text
# from your browser into a text file on your computer.
# You can use the count() method to find out how many times a word or
# phrase appears in a string. For example, the following code counts the number
# of times 'row' appears in a string:
#
# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3
try:
    with open('WisdomWyW.txt', 'r', encoding="utf8") as file_object:
        content = file_object.read()
except FileNotFoundError:
    print("The file you're are looking for is not in this directory")
else:
    lowercase_content = content.lower()
    print(lowercase_content.count("the"))
    print(lowercase_content.count("then"))
    print(lowercase_content.count("there"))
    print(lowercase_content.count("the "))


#
# Notice that converting the string to lowercase using lower() catches
# all appearances of the word you’re looking for, regardless of how it’s
# formatted.
# Write a program that reads the files you found at Project Gutenberg and
# determines how many times the word 'the' appears in each text. This will be
# an approximation because it will also count words such as 'then' and 'there'.
# Try counting 'the ', with a space in the string, and see how much lower your
# count is.

try:
    with open('WisdomWyW.txt', 'r', encoding="utf8") as file_object:
        content = file_object.read()
except FileNotFoundError:
    print("The file you're are looking for is not in this directory")
else:
    lowercase_content = content.lower()
    print(lowercase_content.count("the"))
    print(lowercase_content.count("then"))
    print(lowercase_content.count("there"))
    print(lowercase_content.count("the "))
