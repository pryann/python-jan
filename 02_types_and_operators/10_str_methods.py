# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

print("hello" + " world")  # concatenation
print("hello" * 3)  # repetition

# str is a sequence type, sequence of characters
name = "johnny"
# len is not a method of str, but a built-in function
print(f"length: {len(name)}")
print(f"first char: {name[0]}")
# IndexError: string index out of range
# print(f"first char: {name[4]}")
# TypeError: 'str' object does not support item assignment
# name[0] = "J"

print(f"capitalized: {name.capitalize()}")
print(f"upper: {name.upper()}")
print(f"find chr index: {name.find('o')}")
print(f"count  of 'n': {name.count('n')}")
print(f"replace 'n' to 'N': {name.replace('n', 'N')}")
print(f"remove whitespace: {' John     '.strip()}")
