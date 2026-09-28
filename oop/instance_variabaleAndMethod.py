class Dog:
    def __init__(self, name, breed):
        # INSTANCE VARIABLES (unique to each dog)
        self.name = name
        self.breed = breed

    # INSTANCE METHOD (uses 'self' to access this specific dog's data)
    def bark(self):
        return f"{self.name} the {self.breed} says Woof!"


# Creating two separate instances (objects)
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

# Each object holds its own instance variable data
print(dog1.name)  
print(dog2.name) 

# Calling instance methods
print(dog1.bark())  # Output: Buddy the Golden Retriever says Woof!
print(dog2.bark())  # Output: Max the Bulldog says Woof!