# first_name = "John"
# last_name = "Doe"
# age = 33

# print(first_name, last_name, age)

# Unpacking, the count of the variables must match the count of the values in the iterable
first_name, last_name, age = "John", "Doe", 33
print(first_name, last_name, age)


# data swap
a = 5
b = 10

# use temporary variable
# tmp = a
# a = b
# b = tmp

a, b = b, a
print(a, b)

# unpacking strings
abc = "abc"
a, b, c = abc
print(a, b, c)

text = "Csáó Bella"
# optionally use _ for unused values
first, *_, last = text
print(first, last)

# unpacking lists
user = ["John", "Doe", 33]
first_name, last_name, age = user
print(first_name, last_name, age)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, second, *_ = numbers
print(first, second)
