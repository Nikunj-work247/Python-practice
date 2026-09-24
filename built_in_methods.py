# Common built-in methods for lists, strings, dictionaries, and sets

# List methods
numbers = [3, 1, 2]
numbers.append(4)
print("after append:", numbers)

numbers.insert(0, 0)
print("after insert:", numbers)

numbers.sort()
print("after sort:", numbers)

numbers.reverse()
print("after reverse:", numbers)

numbers.pop()
print("after pop:", numbers)

numbers.remove(0)
print("after remove:", numbers)

numbers.clear()
print("after clear:", numbers)

# String methods
message = "  hello python  "
print("upper:", message.upper())
print("lower:", message.lower())
print("strip:", message.strip())
print("split:", message.strip().split())
print("replace:", message.replace("python", "world"))
print("find:", message.find("hello"))

# Dictionary methods
student = {"name": "Aisha", "age": 20}
print("get:", student.get("name"))
print("keys:", student.keys())
print("values:", student.values())
print("items:", student.items())

student.update({"city": "Lagos"})
print("after update:", student)

student.pop("age")
print("after pop:", student)

student.clear()
print("after clear:", student)

# Set methods
set_numbers = {10, 20, 30}
set_numbers.add(40)
print("after add:", set_numbers)

set_numbers.remove(10)
print("after remove:", set_numbers)

set_numbers.discard(99)
print("after discard:", set_numbers)

popped_value = set_numbers.pop()
print("popped value:", popped_value)
print("set after pop:", set_numbers)

set_numbers.clear()
print("final set:", set_numbers)
