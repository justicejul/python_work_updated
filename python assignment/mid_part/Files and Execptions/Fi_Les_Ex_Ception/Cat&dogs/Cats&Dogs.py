# Make two files, cats.txt and dogs.txt.
# Store at least three names of cats in the first file and three names of dogs in the second file.
# Write a program that tries to read these files and print the contents of the file to the screen.
# Wrap your code in a try-except block to catch the FileNotFound error,
# and print a friendly message if a file is missing.
# Move one of the files to a different location on your system, and make sure the code in the except
# block executes properly.
try:
    with open('cat.txt', 'r') as file_object:
        content = file_object.read()
except FileNotFoundError:
    pass
    # print("The file you are looking for is not here please check somewhere else")
else:
    print(content)

print("\n")

try:
    with open('dog.txt', 'r') as file_object:
        content = file_object.read()
except FileNotFoundError:
    print("The file you are looking for is not here please check somewhere else")
else:
    print(content)
