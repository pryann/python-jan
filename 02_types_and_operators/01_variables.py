# immutable
# variable name conventions: lowercase_with_underscores
# variable names cannot start with a number or special character
# reserved words (keywords) cannot be used as variable names
# do no start with underscore (_), it used for special purposes in Python
age = 10

print(age)
print(age + 1)

age = 15
print(age)

# keywords
print(help("keywords"))

# tax = 27 # not recommended, as 'tax' is a common term
# python use snake_case for variable names
standard_hungarian_tax_rate_in_percent = 27
print(standard_hungarian_tax_rate_in_percent)

# constant variable, in terms , by convention
# all uppercase with underscores
# python not supports true constant variables
TOKEN = "asdasdasdasdasdasdasd"  # constant variable by convention
TOKEN = "qweqweqweqweqwe"  # but can be changed
