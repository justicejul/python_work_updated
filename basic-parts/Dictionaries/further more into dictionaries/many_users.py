users = {
 'aeinstein': {
              'first': 'albert',
              'last': 'einstein',
              'location': 'princeton',
              },

 'mcurie':   {
             'first': 'marie',
             'last': 'curie',
             'location': 'paris',
             },
 }
# for username, user_info in users.items():
#     print(f"\nUsername: {username}")
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")

for K,V in users.items():
    first_name = V['first']
    second_name = V['last']
    location = V['location']
    print(f"Full-name: {first_name} {second_name}")
    print(f"Locaation: {location}")


