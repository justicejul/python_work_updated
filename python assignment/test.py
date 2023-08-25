
# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell'],
#     }

# for name, languages in favorite_languages.items():
#     for language in languages:
#         if len(languages) <= 1:
#             print(f"\n{name.title()}'s favorite languages is {language.title()}")
#         elif len(languages) > 1:
#             print(f"\n{name.title()}'s favorite languages are: {language.title()}")
            



# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell'],
#     }
# for name, languages in favorite_languages.items():
#     if len(languages) == 1:
#         print(f"\n{name.title()}'s favorite languages is:")
#     else:
#         print(f"\n{name.title()}'s favorite languages are:")

#     for language in languages:
#         print(f"\t{language.title()}")


# name = ['kenny', 'joshua', 'tim']
# for n in name:
#     print(f"my name is {n}")




# numbers = []
# for x in range(10):
#     numbers.append(x)
# print(len(numbers))



# numbers = {
#     'justice': [8, 18],
#     'blessing': [17, 5],
#     'james' : [7],
#     'usman': [19, 35],
#     'junior': [19],
#     'juliet' : [3, 11],
#     # 'vivian' : 3,
#     'Pablo' : [16,7],
#     # 'elizabeth' : 18,
#      }

# for names, nums in numbers.items():
#     if len(nums) != 1:
#         print(f"\n{names.title()} favourite numbers are:")
#         for num in nums:
#             print(f"\t{num}")
#     else:
#         print(f"\n{names.title()} favourite numbers is:")
#         print(f"\t{num}")


# for names, nums in numbers.items():
#     if len(nums) > 1:
#         print(f"\n{names.title()} favourite numbers are:")
#         for num in nums:
#             print(f"\t{num}")
#     # else:
#     #     print(f"\n{names.title()} favourite numbers is:")
#     #     for num in nums:
#     #         print(f"\t{num}")




# for x in range(10):
#     print(x)
#     if x == 5:
#         break


# num = 0
# while num <= 6:
#     num =+ 1
#     if num > 6:
#         break
#     print(num)


# x = 0
# while x < 11:
#     if x == 6:
#         break
#     print(x)
#     # x += 1



# names = ['Nzube', 'Jake', 'Pablo', 'Jennifer', 'Emmanuella']
# for name in names:
#     names.append('Godwin')
#     print(name)
#     print(names)

# names = ['Nzube', 'Jake', 'Pablo', 'Jennifer', 'Emmanuella']
# while names:
#     name = names.pop()
#     print(name)
#     break


# def add(a,b):
# 	a = "",
# 	b = "",
# 	int(a),
# 	int(b),
# 	a + b

# add(2+2)


# def greet_user(username):
#     """Display a simple greeting."""
#     print(f"Hello, {username.title()}!")
 
# greet_user('justice')
  
# def dictionary(name, key, value):
#     name = {}
#     name[key] = value

# dictionary(justice, 'work', 'developer')
# print(justice)


# def describe_pet(animal_type, pet_name='harry'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(animal_type='hamster', pet_name='james')

# def describe_pet(animal_type, pet_name='harry'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(animal_type='hamster')

# def describe_pet(pet_name="fred", animal_type="chicken"):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet()

# def describe_pet(animal_type, pet_name='harry'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(animal_type='hamster', pet_name='james')
# describe_pet(animal_type='Janguar', pet_name='justice')


# def describe_pet(pet_name, animal_type="chicken"):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
# describe_pet(animal_type='peacock', pet_name='Ben')

my_list = [1,2,3,4,5,6,7,8,9]

print(len(1))

# def get_num(c):
#     for a in my_list:
#         for b in my_list:
#             if a + b == c:
#                  return a, b
#
# answer = get_num(12)
# print(answer)