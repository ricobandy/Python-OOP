class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount
    

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        self.interestRate = interestRate
        super().__init__(title, balance)

    def interestAmount(self):
        return (self.balance * self.interestRate) / 100
        

    