# Python data types and basic behavior

# int: whole numbers
age = 25
print("int example:", age)
print("type(age):", type(age))

# float: decimal numbers
price = 10.5
print("float example:", price)
print("type(price):", type(price))

# complex: numbers with a real and imaginary part
complex_number = 2 + 3j
print("complex example:", complex_number)
print("real part:", complex_number.real)
print("imaginary part:", complex_number.imag)

# string: text
name = "Alice"
print("string example:", name)
print("type(name):", type(name))

# bool: True or False
is_student = True
print("bool example:", is_student)
print("type(is_student):", type(is_student))

# None: no value
empty_value = None
print("None example:", empty_value)
print("type(empty_value):", type(empty_value))

# Type conversion examples
number_text = "42"
converted_number = int(number_text)
print("converted number:", converted_number)

float_value = 7.8
converted_int = int(float_value)
print("float to int:", converted_int)

boolean_value = bool(0)
print("bool(0):", boolean_value)

# Basic behavior example
print("string length:", len("Python"))
print("two strings together:", "Hello" + " World")
