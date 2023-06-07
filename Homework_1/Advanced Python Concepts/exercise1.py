"""
Write a Python class called BankAccount with methods for depositing, withdrawing,
and checking the account balance.
"""
from uuid import uuid4
from faker import Faker

class BankAccount:
    def __init__(self,name: str, account_number: str, amount : float = 0) -> None:
        self.name = name
        self.account_number = account_number
        self.amount = amount

    def depositing(self, amount: float) -> float:
        try:
            if amount > 0:
                self.amount += amount
                return self.amount
            else:
                raise ValueError("Invalid Amount! Please Enter a Positive Amount")
        except Exception as e:
            print(e)
    
    def withdraw(self, amount: float) -> float:
        try:
            if  0 < amount <= self.amount:
                    self.amount -= amount
                    print(f"Successfull Transaction, Withdrew {amount} dollars from {self.account_number} account")
            else:
                raise ValueError("Failed Transaction Insufficient Funds!")
        except Exception as e:
            print(e)

    
    def balance(self):
        print(f"This account has {self.amount} dollars!")
    

fake = Faker()

account1 = BankAccount(fake.name(), uuid4() )
print(account1.account_number)
account1.depositing(100)
account1.withdraw(60)
print(account1.amount)
account1.balance()

