# 1. Írj egy függvényt, amely egy számokat tartalmazó listát kap bemenetként, majd visszatér egy új listával, amelyben a számok duplája szerepel


def duplicate_numbers(numbers):
    # return [i * 2 for i in numbers]
    duplicated = []
    for number in numbers:
        duplicated.append(number * 2)
    return duplicated


print(duplicate_numbers([1, 2, 3, 4, 5]))

# 2. Készíts egy függvényt, amely paraméterként kap egy listát és visszaadja azt a listát,amely csak a páros számokat tartalmazza! A megoldás során comprehensiont használj!


def filter_even_numbers(numbers):
    # even_numbers = []
    # for number in numbers:
    #     if number % 2 == 0:
    #         even_numbers.append(number)
    # return even_numbers
    return [n for n in numbers if n % 2 == 0]


print(filter_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# 3. Készíts egy függvényt, amely paraméterként kap két listát és visszaadja azt a listát, amely csak azokat az elemeket tartalmazza, amelyek mindkét listában szerepelnek! Comprehensiont használj!


def intersect_lists(list1, list2):
    # intersect = []
    # for item in list1:
    #     if item in list2:
    #         intersect.append(item)
    # return intersect
    return [i for i in list1 if i in list2]


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print(intersect_lists(list1, list2))
