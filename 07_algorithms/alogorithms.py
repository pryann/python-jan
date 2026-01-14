# minimum kiválasztása egy listából
values = [1, 2, 3, 4, 5, 5]


def get_minimum(values):
    # validation
    if len(values) == 0:
        return None

    minimum = values[0]
    for i in range(1, len(values)):
        if values[i] < minimum:
            minimum = values[i]
    return minimum


print(get_minimum(values))
print(min(values))  # beépített függvény


def get_maximum(values):
    # validation
    if len(values) == 0:
        return None

    maximum = values[0]
    for i in range(1, len(values)):
        if values[i] > maximum:
            maximum = values[i]
    return maximum


print(get_maximum(values))
print(max(values))


def summa(values):
    summa = 0
    for value in values:
        summa += value
    return summa


print(summa(values))
print(sum(values))  # beépített függvény


def average(values):
    return summa(values) / len(values)


print(average(values))
print(sum(values) / len(values))  # beépített függvények kombinál


# count
def count_values(values, search):
    # count = 0
    # for value in values:
    #     if value == search:
    #         count += 1
    # return count
    return len([v for v in values if v == search])


print(count_values(values, 5))
print(values.count(5))


# kiválasztás: tudjuk, hgoy benne van a listában, kell az index
def find_index(values, search):
    for i in range(len(values)):
        if values[i] == search:
            return i


print(find_index(values, 4))
print(values.index(4))


# eldöntés
def is_contains(values, search):
    # for value in values:
    #     if value == search:
    #         return True
    # return False
    return len([v for v in values if v == search]) > 0


print(is_contains(values, 3))
print(3 in values)
