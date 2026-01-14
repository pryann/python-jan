# unordered
# mutable
# contains unique elements
my_set = {1, 2, 3}

print(my_set)

my_set.add(4)
print(my_set)

my_set.update([4, 5, 6])
print(my_set)

# raise KeyError if the element is not found
my_set.remove(6)
print(my_set)

# does not raise an error if the element is not found
my_set.discard(10)
print(my_set)

# remove a random element
my_set.pop()
print(my_set)

# REALLY USEFUL FUNCTION
numbers = [1, 2, 3, 4, 1, 2, 3, 3, 4]
unique_number = list(set(numbers))
print(unique_number)  
