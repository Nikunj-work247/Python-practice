# Loops and control statements

# for loop example
print("for loop:")
for number in range(1, 4):
    print(number)

# while loop example
print("while loop:")
count = 1
while count <= 3:
    print(count)
    count += 1

# nested loops example
print("nested loops:")
for outer in range(1, 3):
    for inner in range(1, 3):
        print(f"outer={outer}, inner={inner}")

# break: stop the loop immediately
print("break example:")
for value in range(1, 6):
    if value == 3:
        break
    print(value)

# continue: skip the current item and continue
print("continue example:")
for value in range(1, 6):
    if value == 3:
        continue
    print(value)

# pass: do nothing and continue normally
print("pass example:")
for value in range(1, 4):
    if value == 2:
        pass
    print(value)

# loop else example
print("for else example:")
for value in range(1, 4):
    print(value)
else:
    print("Loop finished without break.")

# Simple comparison of break, continue, pass
print("Difference between break, continue, and pass:")
for x in range(1, 5):
    if x == 2:
        print("continue skips 2")
        continue
    if x == 3:
        print("break stops before 3")
        break
    if x == 1:
        print("pass does nothing here")
        pass
    print("current value:", x)
