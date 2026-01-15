def remove_duplicates(input_list: list) -> list:
    return list(set(input_list))


def sort_list(input_list: list) -> list:
    input_list.sort()
    return input_list

    # input_list_copy = input_list.copy()
    # input_list_copy.sort()
    # return input_list_copy
