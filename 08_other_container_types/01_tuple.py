# immutable
# faster than list
# ordered
# allow dupicated members
rgb = (255, 0, 0)

print("Red:", rgb[0])
# TypeError: 'tuple' object does not support item assignment
# rgb[0] = 128

print(rgb.count(0))
print(rgb.index(255))

rgb_list = list(rgb)
rgb_list[0] = 128
rgb = tuple(rgb_list)

print("Modified tuple:", rgb)


# fmt: off
numbers = (1)
print(type(numbers)) # <class 'int'>

numbers = (1,)
print(type(numbers)) # <class 'tuple'>
