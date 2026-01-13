# OTHER LANGUAGES: pass by values & pass by reference
# PYTHON: pass by object reference

# MEMORY
# -----------------

# 3300      0x0001    <----------- age
#                     <----------- age_copy
# -----------------

age = 3300
age_copy = age

print(("age: ", age, id(age)))
print(("age_copy: ", age_copy, id(age_copy)))

age = 18
print(("age: ", age, id(age)))
print(("age_copy: ", age_copy, id(age_copy)))

# MEMORY
# -----------------

# 18        0x0001    <----------- age
#
# -----------------

# 3300      0x0001    <----------- age_copy
#
# -----------------
