# import the entire module
# import math


# print(math.pi)
# print(math.sqrt(16))

# import specific attributes from a module
# from math import sqrt, pi

# print(pi)
# print(sqrt(16))

# Do not use wildcard imports in real projects
# from math import *

# print(pi)
# print(sqrt(16))

# alias the module name
# import math as mathematical

# print(mathematical.pi)
# print(mathematical.sqrt(16))

# alias specific attributes from a module
from math import sqrt as square_root, pi as PI

print(PI)
print(square_root(16))
