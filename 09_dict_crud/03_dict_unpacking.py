user_dict = {
    "name": "John Doe",
    "age": 33,
    "status": "active",
}

# Unpacking dictionary keys into variables
name, age, status = user_dict
print(name, age, status)

name, age, status = user_dict.values()
print(name, age, status)
