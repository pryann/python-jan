users = [
    {
        "id": 1,
        "first_name": "Adlai",
        "last_name": "Lydall",
        "email": "alydall0@quantcast.com",
    },
    {
        "id": 2,
        "first_name": "Parke",
        "last_name": "Shafier",
        "email": "pshafier1@rakuten.co.jp",
    },
    {
        "id": 3,
        "first_name": "Crystal",
        "last_name": "Whinray",
        "email": "cwhinray2@cbslocal.com",
    },
    {
        "id": 4,
        "first_name": "Preston",
        "last_name": "Howard",
        "email": "phoward3@sourceforge.net",
    },
    {
        "id": 5,
        "first_name": "Julie",
        "last_name": "Frome",
        "email": "jfrome4@godaddy.com",
    },
]


def generate_new_id():
    max_id = 0
    for user in users:
        if user["id"] > max_id:
            max_id = user["id"]
    return max_id + 1


# CRUD Operations
# Create Read Update Delete


# Read


def get_users():
    return users


def find_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    # optional, if you want to be explicit
    # return None


# Create
def create_user(user_payload):
    # it works only if users is ordered by user ids
    # new_id = users[-1]["id"] + 1
    new_user = {"id": generate_new_id()}
    new_user.update(user_payload)
    users.append(new_user)
    return users[-1]


# Update
def update_user(user_id, user_payload):
    user = find_user_by_id(user_id)
    if user is not None:
        index = users.index(user)
        users[index].update(user_payload)
        return users[index]
    # return None


# Delete
def remove_user(user_id):
    user = find_user_by_id(user_id)
    if user is not None:
        users.remove(user)
    # you can return the removed user if needed
    return user


# print("All users:", get_users())
# print("User with ID 3:", find_user_by_id(10))
# print("before update", find_user_by_id(2))
# print("after update", update_user(2, {"first_name": "John"}))
# print(
#     "new user: ",
#     create_user(
#         {"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"}
#     ),
# )
print("remove", remove_user(3))
print(users)
