print(True, type(True))
print(False, type(False))

is_item_available = True
print(is_item_available, type(is_item_available))

item_price = 100
money = int(input("Please enter the amount of money you have: "))
# <, >, <=, >=, ==, !=
print("Can you buy the item?", money >= item_price)
