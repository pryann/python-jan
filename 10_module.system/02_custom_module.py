# from my_package.my_module import greetings, farewell

# print(greetings("Alice"))
# print(farewell("Bob"))

import my_package.my_module

print(my_package.my_module.greetings("Alice"))
print(my_package.my_module.farewell("Bob"))
