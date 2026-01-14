# paraméter lista, formális
# NoneType, egy értéke van: None
# minden függvény visszatér valamilyen értékkel, ha nem adunk meg return utasítást, akkor a visszatérési érték None
from operator import add


def greetings(name):
    return f"Hello {name}!"


# argumentum, aktuális
# greetings("Alice")
# greetings("Bob")
print(greetings("Gergő"))


# default paraméter érték
def calculate_gross_price(price, vat_rate_percent=27):
    return price * (1 + vat_rate_percent / 100)


print(calculate_gross_price(1000))
print(calculate_gross_price(1000))
print(calculate_gross_price(2000, 5))


def add_item_to_basket(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket


# print(add_item_to_basket("apple", []))
# print(add_item_to_basket("orange", []))
# basket = []
# print(add_item_to_basket("apple", basket))
# print(add_item_to_basket("orange", basket))

print(add_item_to_basket("apple"))
print(add_item_to_basket("orange"))
