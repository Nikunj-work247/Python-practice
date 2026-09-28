class BankAccount:
    def __init__(self,owner):
        self.owner = owner
acc = BankAccount("Alice")
print(acc.owner)