x1 = {"a", "b", "c"}
x2 = {"b", "c", "d"}

print(x1.union(x2))  # {'a', 'b', 'c', 'd'}
print(x1.intersection(x2))  # {'b', 'c'}
print(x1.difference(x2))  # {'a'}
print(x1.symmetric_difference(x2))  # {'a', 'd'}
print(x1.isdisjoint(x2))  # False
print(x1.issubset({"a", "b", "c", "d"}))
print(x1.issuperset({"a", "b"}))

# all methods have an operator equivalent
print(x1 | x2)  # union
print(x1 & x2)  # intersection
print(x1 - x2)  # difference
print(x1 ^ x2)  # symmetric difference
print(x1 <= {"a", "b", "c", "d"})  # issubset
print(x1 >= {"a", "b"})  # issuperset

