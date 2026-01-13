# str props, methods
full_name = "Gergely Kiss"
print(full_name.upper())
print("Gergely Kiss".upper())

name = "Gergely"
age = 30

# oldschool way
me = "My name is " + name + ", and I'm " + str(age) + " years old."
print(me)


# better way: format method
better_me = "My name is {}, and I'm {} years old.".format(name, age)
print(better_me)

# best way: f-strings (formatted string literals)
best_me = f"My name is {name}, and I'm {age} years old."
print(best_me)
