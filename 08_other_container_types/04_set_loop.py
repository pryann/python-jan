my_set = {10, 2, 3, 4}

# iterate through a set, order is not guaranteed
for i in my_set:
    print(i)

# i is a generated index, not a real index
for i, v in enumerate(my_set):
    print(f"index: {i}, value: {v}")
