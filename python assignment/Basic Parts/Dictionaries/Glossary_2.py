# Now that you know how to loop through a dictionary, clean 
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When 
# you’re sure that your loop works, add five more Python terms to your glossary. 
# When you run your program again, these new words and meanings should 
# automatically be included in the output.



programming_dictionary = {
        'methods':"are small functions that work with strings, whether they're words or sentences",
        'lists'	: 'in python, are used to  store lists of items or information' ,
        'white_spaces' : 'are non-printing charactersthat affect the positioning of an elements',
        'Tuples' :  'can also be known as "immutable list", they\'re are like lists but they cannot be changed',
        'Loops' : 'are used to print out values singularly in a vertical form',
        'Dictionaries' : 'are  used to store information in form of key and value pair',
        'sets' : 'are group of elements which are unordered, unindexed and doesn\'t allow duplicate',
        'keys() method' : 'is a method used in printing keys in key-value pairs in dictionaries'  ,
        'values() method' : 'is a method used in printing values in key-value pairs in dictionaries',
        'get() method' : "is a method used to print a default value when a key doesn\'t exist in key-value pair",
        }

for word, meaning in programming_dictionary.items():
        print(f"{word} {meaning} \n")