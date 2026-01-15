def generate_new_id():
    max_id = 0
    for user in users:
        if user["id"] > max_id:
            max_id = user["id"]
    return max_id + 1


def get_users():
    return users


def find_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user


def create_user(user_payload):
    new_user = {"id": generate_new_id()}
    new_user.update(user_payload)
    users.append(new_user)
    return users[-1]


def update_user(user_id, user_payload):
    user = find_user_by_id(user_id)
    if user is not None:
        index = users.index(user)
        users[index].update(user_payload)
        return users[index]


def remove_user(user_id):
    user = find_user_by_id(user_id)
    if user is not None:
        users.remove(user)
    return user
