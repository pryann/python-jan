int_value = 10
float_value = 3.14

converted_int = int(float_value)
print(converted_int)
conerted_float = float(int_value)
print(conerted_float)

str_value = "-100"
print(type(str_value))
# converted only if it is a valid representation of the target type
converted_str_to_int = int(str_value)
print(type(converted_str_to_int))

str_value = "100.56"
# converted only if it is a valid representation of the target type
converted_str_to_float = float(str_value)
print(type(converted_str_to_float))

int_value = 255
# str return "255"
# type returns <class 'str'>
# print prints the <class 'str'> to to stdout
print(type(str(int_value)))  # decimal string representation
