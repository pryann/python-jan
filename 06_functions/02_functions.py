# use pass statement to create empty functions
from turtle import Vec2D


def calculate_gross_price():
    pass


def apply_discount():
    pass


def apply_coupon():
    pass


# V1
# def is_even_number(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False


# V2
# def is_even_number(number):
#     if number % 2 == 0:
#         return True
#     return False


# V3
# def is_even_number(number):
#     return number % 2 == 0


# print(is_even_number(4))
# print(is_even_number(5))


# V4 - ternary
def is_even_number(number):
    return "even" if number % 2 == 0 else "odd"


print(is_even_number(4))
print(is_even_number(5))


# Rekurzió: önmagát hívó függvény
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
    # if b == 0:
    #     return a
    # else:
    #     return gcd(b, a % b)


print(gcd(48, 18))
print(gcd(33, 11))
