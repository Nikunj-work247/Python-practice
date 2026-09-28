class InsufficientBalanceError(Exception):
    """Custom Exception jab account balance kam ho"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Low Balance! Required: ₹{amount}, Available: ₹{balance}")


def process_atm_withdrawal(account_balance, withdraw_amount):
    print("\n--- Transaction Started ---")
    
    try:
        if withdraw_amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero!")
            
        if withdraw_amount > account_balance:
            raise InsufficientBalanceError(account_balance, withdraw_amount)
            
        remaining_balance = account_balance - withdraw_amount

 
    except InsufficientBalanceError as e:
        print(f"[EXCEPT 1] Transaction Failed: {e}")

 
    except ValueError as e:
        print(f"[EXCEPT 2] Invalid Input: {e}")

    except Exception as e:
        print(f"[EXCEPT 3] Unexpected Error Occurred: {e}")

    else:
        print(f"[ELSE] Transaction Successful!")
        print(f"[ELSE] Please collect your cash: ₹{withdraw_amount}")
        print(f"[ELSE] Remaining Balance: ₹{remaining_balance}")

    finally:
        print("[FINALLY] Ejecting ATM Card...")
        print("[FINALLY] Session Closed safely.")

process_atm_withdrawal(account_balance=5000, withdraw_amount=2000)

process_atm_withdrawal(account_balance=1000, withdraw_amount=3000)

process_atm_withdrawal(account_balance=5000, withdraw_amount=-500)