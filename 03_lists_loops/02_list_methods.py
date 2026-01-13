yearly_salaries = [45_000, 50_000, 60_000, 75_000, 80_000]
print("id:", id(yearly_salaries))

# update a single value
yearly_salaries[0] = 45_000 * 1.1
print("after update:", yearly_salaries)
print("id:", id(yearly_salaries))

# delete index 2
del yearly_salaries[2]
print("after delete:", yearly_salaries)

yearly_salaries.append(90_000)
print("after append:", yearly_salaries)

yearly_salaries.extend([100_000, 120_000])
print("after extend:", yearly_salaries)

yearly_salaries.insert(1, 66_667)
print("after insert:", yearly_salaries)

# remove value
yearly_salaries.remove(66_667)
print("after remove:", yearly_salaries)

# remove and return last item
yearly_salaries.pop()
print("after pop:", yearly_salaries)

yearly_salaries.append(50_000)
print("after append:", yearly_salaries)

print("count of 50_000:", yearly_salaries.count(50_000))

# sort is mutating the original list too
yearly_salaries.sort(reverse=True)
print("after sort:", yearly_salaries)

# reverse is mutating the original list too
yearly_salaries.reverse()
print("after reverse:", yearly_salaries)

user = ["John", "Doe", "teacher", "33 year old"]
print(user)
# join is a str method
user_str = ", ".join(user)
print("joined string:", user_str)
