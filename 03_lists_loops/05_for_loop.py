# for keyword variable iterable:
# sequence : 0..9
for i in range(10):
    print(i)

print("----")

for i in range(5, 10):
    print(i)

print("----")

for i in range(5, 100, 5):
    print(i)

print("----")

for i in range(100, -1, -5):
    print(i)

print("----")

yearly_salaries = [50000, 60000, 70000]

for yearly_salary in yearly_salaries:
    print(yearly_salary)

print("----")

# not often used, but possible
for index in range(len(yearly_salaries)):
    print("index:", index, "yearly_salary:", yearly_salaries[index])

print("----")

# index is a generated variable, starts at 0 and increments by 1, NOT THE INDEX OF THE LIST!
for index, yearly_salary in enumerate(yearly_salaries):
    print("index:", index, "yearly_salary:", yearly_salary)
