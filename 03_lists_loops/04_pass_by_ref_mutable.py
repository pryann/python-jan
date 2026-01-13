# MEMORY
# -----------------------
#
# [50000, 60000, 70000]     <------ yearly_salaries
#                           <------ yearly_salaries_copy
# -----------------------   <------ yearly_salaries_copy_2

import numbers


yearly_salaries = [50000, 60000, 70000]
yearly_salaries_copy = yearly_salaries

print(("yearly_salaries: ", yearly_salaries, id(yearly_salaries)))
print(("yearly_salaries_copy: ", yearly_salaries_copy, id(yearly_salaries_copy)))

# mutate the list
yearly_salaries[0] = 0
print(("yearly_salaries: ", yearly_salaries, id(yearly_salaries)))
print(("yearly_salaries_copy: ", yearly_salaries_copy, id(yearly_salaries_copy)))

# mutate the list by appending
yearly_salaries_copy.append(1)
print(("yearly_salaries: ", yearly_salaries, id(yearly_salaries)))
print(("yearly_salaries_copy: ", yearly_salaries_copy, id(yearly_salaries_copy)))

yearly_salaries_copy_2 = yearly_salaries_copy
yearly_salaries_copy_2.insert(2, 99999)
print(("yearly_salaries: ", yearly_salaries, id(yearly_salaries)))
print(("yearly_salaries_copy: ", yearly_salaries_copy, id(yearly_salaries_copy)))
print(("yearly_salaries_copy_2: ", yearly_salaries_copy_2, id(yearly_salaries_copy_2)))

print("--- Reassign yearly_salaries to a new list ---")
yearly_salaries = [1, 2, 3]
print(("yearly_salaries: ", yearly_salaries, id(yearly_salaries)))
print(("yearly_salaries_copy: ", yearly_salaries_copy, id(yearly_salaries_copy)))
print(("yearly_salaries_copy_2: ", yearly_salaries_copy_2, id(yearly_salaries_copy_2)))

print("--- COPY ---")
# MEMORY
# -----------------------
# [1,2,3]                   <------ numbers_list
# -----------------------
# [1,2,3]                   <------ numbers_list_copy
# -----------------------

numbers_list = [1, 2, 3]
# numbers_list_copy = numbers_list.copy()
numbers_list_copy = numbers_list[:]
print(numbers_list, id(numbers_list))
print(numbers_list_copy, id(numbers_list_copy))

numbers_list.append(4)
numbers_list_copy.append(5)
print(numbers_list, id(numbers_list))
print(numbers_list_copy, id(numbers_list_copy))
