class BankAccount:
    def __init__(self,balance,owner=None):
        self.balance=balance
        self.owner=owner
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds")
        else:
            self.balance-=amount
    def get_balance(self):
        return f"Balance: {self.balance}"
acc=BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
print(acc.get_balance())