user_dict = {
    "name": "John Doe",
    "age": 33,
    "hobbies": ["reading", "traveling", "swimming"],
}

print(user_dict)
# Accessing values
print(user_dict["name"])

# updating values
user_dict["age"] = 18
print(user_dict["age"])

# Adding new key-value pairs
user_dict["status"] = "active"
print(user_dict)

user_dict.update({"salary": 50_000, "status": "unverified"})
print(user_dict)

# removing key-value pairs
user_dict.pop("hobbies")
print(user_dict)
