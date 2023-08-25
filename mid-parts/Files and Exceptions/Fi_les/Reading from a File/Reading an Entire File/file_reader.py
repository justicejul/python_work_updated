# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())
  



# # USING FOR LOOP ON IT

# filename = "pi_digits.txt"

# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())





# MAKING A LIST OF LINES FROM A FILE

# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()

# print(lines)

# print("\n")

# for line in lines:
#     print(line.rstrip())




filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))





filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

