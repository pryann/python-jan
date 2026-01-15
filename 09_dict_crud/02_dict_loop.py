user_dict = {
    "name": "John Doe",
    "age": 33,
    "status": "active",
}

# Return a dict_keys object NOT LIST!!!
print("keys: ", user_dict.keys(), type(user_dict.keys()))

# Return a dict_values object NOT LIST!!!
print("values: ", user_dict.values(), type(user_dict.values()))

# Return a dict_items object NOT LIST!!!
print("items: ", user_dict.items(), type(user_dict.items()))

# Looping through keys
for key in user_dict:
    print(key)
    # print(user_dict[key])

for key in user_dict.keys():
    print(key)
    # print(user_dict[key])

# Looping through values
for value in user_dict.values():
    print(value)

# Looping through key-value pairs
for key, value in user_dict.items():
    print(key, value)

# Looping with numeric index
# for i in range(len(user_dict)):
#     print(i)

# key is a generic index here, not the actual dict key
# value is the actual dict key
for key, value in enumerate(user_dict):
    print(key, value)
