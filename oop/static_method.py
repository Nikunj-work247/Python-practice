class Calculator:
    @staticmethod
    def add(a, b):
        return a + b


#no need to create an object
result = Calculator.add(5, 3)
print(result)  