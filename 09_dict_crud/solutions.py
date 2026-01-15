# 1. Írj egy függvényt, ami egy set és egy tuple elemeit fűzi össze! A függvény bemenete egy set és egy tuple. A függvény visszatérési értéke egy új set, amely a bemeneti set és tuple elemeit tartalmazza!


def concat_set_tuple(input_set: set, input_tuple: tuple) -> set:
    # return input_set.union(input_tuple)
    concated = []
    # you can use list or set
    # concated = set()
    for set_item in input_set:
        concated.append(set_item)

    for tuple_item in input_tuple:
        concated.append(tuple_item)

    return set(concated)
    # return input_set.union(input_tuple)


print(concat_set_tuple({1, 2, 3}, (3, 4, 5)))

# 2. Írj egy Python függvényt, amely kap egy szótárat és egy kulcsot, majd visszaadja az adott kulcshoz tartozó értéket, vagy ha nincs ilyen kulcs, akkor a "Nincs ilyen kulcs" üzenetet.


def get_value_from_dict(input_dict: dict, key: str) -> any:
    # if key in input_dict:
    #     return input_dict[key]
    # else:
    #     return "Nincs ilyen kulcs"

    return input_dict[key] if key in input_dict else "Nincs ilyen kulcs"


print(get_value_from_dict({"a": 1, "b": 2}, "a"))
print(get_value_from_dict({"a": 1, "b": 2}, "c"))


# 3. Írj egy függvényt, amely egy szótárból eltávolítja azokat a kulcs-érték párokat, amelyek kulcsa nem szerepel egy megadott kulcsokat tartalmazó listában!
def remove_items_from_dict(input_dict: dict, keys_to_keep: list) -> dict:
    # cleaned_dict = {}
    # for key in keys_to_keep:
    #     if key in input_dict:
    #         cleaned_dict[key] = input_dict[key]
    # return cleaned_dict
    return {key: input_dict[key] for key in keys_to_keep if key in input_dict}


my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
my_list = ["a", "c", "e"]
print(remove_items_from_dict(my_dict, my_list))


# 4. Adott két listát, hozz létre egy olyan listát, amely csak azokat az elemeket tartalmazza, amelyek mindkét listában szerepelnek!
def interset_lists(list1: list, list2: list) -> list:
    # intersect_list = []
    # for i in list1:
    #     if i in list2:
    #         intersect_list.append(i)
    # return intersect_list

    return list(set(list1).intersection(list2))
    # performance optimization:
    # len_list_1 = len(list1)
    # len_list_2 = len(list2)
    # if len_list_1 < len_list_2:
    #     for i in list1:
    #         if i in list2:
    #             intersect_list.append(i)
    # else:
    #     for i in list2:
    #         if i in list1:
    #             intersect_list.append(i)
    # return intersect_list


print(interset_lists([1, 2, 3, 4], [3, 4, 5, 6]))
