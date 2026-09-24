numbers = {1, 2, 3, 4}

print(numbers)

numbers = {1, 2, 2, 3, 3, 4}

print(numbers)

numbers = set()

print(type(numbers))

#operation
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

#union-
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a | set_b)
#intersection
print(set_a & set_b)
print(set_a - set_b)
print(set_a ^ set_b)

numbers = frozenset([1, 2, 3, 4])

print(numbers)
numbers.add()