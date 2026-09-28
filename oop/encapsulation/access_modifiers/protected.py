class BankAccount:
    def __init__(self, owner):
        self._account_type = "Savings"  # Protected attribute

class SavingsAccount(BankAccount):
    def display_type(self):
        print(f"Account type: {self._account_type}")  

acc = SavingsAccount("Bob")
acc.display_type()  

print(acc._account_type) 