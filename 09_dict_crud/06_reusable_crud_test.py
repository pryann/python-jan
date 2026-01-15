from reusable_crud import (
    get_items,
    find_item_by_id,
    create_item,
    update_item,
    remove_item,
)

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
cars = [
    {"id": 1, "company": "Dodge", "model": "Intrepid", "year": 2003},
    {"id": 2, "company": "Oldsmobile", "model": "88", "year": 1998},
    {"id": 3, "company": "Ford", "model": "Galaxie", "year": 1964},
    {"id": 4, "company": "Mercury", "model": "Topaz", "year": 1994},
    {"id": 5, "company": "Chevrolet", "model": "1500", "year": 1993},
]

# print(get_items(users))
# print(get_items(cars))
print(find_item_by_id(3, users))
print(find_item_by_id(3, cars))
print(
    "create user:",
    create_item(
        {"first_name": "Test", "last_name": "User", "email": "testuser@example.com"},
        users,
    ),
)
# print(users)
print(
    "create car:",
    create_item(
        {"company": "Mercedes", "model": "C-Class", "year": 2022},
        cars,
    ),
)
# print(cars)
print(
    "update user:",
    update_item(1, {"first_name": "UpdatedName"}, users),
)
print(
    "update car:",
    update_item(1, {"model": "UpdatedModel"}, cars),
)


print("remove user:", remove_item(2, users))
print("remove car:", remove_item(2, cars))
