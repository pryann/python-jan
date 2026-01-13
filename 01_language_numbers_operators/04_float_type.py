# Float Type
# IEEE 754 standard for floating-point arithmetic
# double precision (64 bits): 1 bit sign, 11 bits exponent, 52 bits fraction

print(10.123)  # 10.123
print(-10.123)  # -10.123
print(type(10.123))  # <class 'float'>

print(type(1.79e308))  # <class 'float'> (maximum float
print(type(5e-324))  # <class 'float'> (minimum positive float)

# special float values
print(float("inf"))  # inf
print(float("-inf"))  # -inf

print(0.1 + 0.2 == 0.3)  # False due to floating-point precision issues
print(0.1 + 0.2)  # 0.30000000000000004
