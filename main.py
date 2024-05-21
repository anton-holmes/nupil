import os

user_name = os.getenv("PATH")
list_path = user_name.split(':')

print(os.system('stat ' + list_path[0]))

print(list_path[0])







    