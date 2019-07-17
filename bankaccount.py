class BankAccount:

    interest_rate = 1.00
    accounts = []

    def __init__ (self):
        self.balance = 0
    
    def deposit(self, monies):
        self.balance += monies

    def withdraw(self, monies):
        self.balance -= monies

    @classmethod
    def create(cls):
        newaccount = BankAccount()
        cls.accounts.append(newaccount)
        return newaccount

    @classmethod
    def total_funds(cls):
        total_balance = 0
        for account in cls.accounts:
            total_balance += account.balance
        return total_balance

    @classmethod
    def interest_time(cls):
        for account in cls.accounts:
            account.balance += (cls.interest_rate / 100) * account.balance
        return account.balance


my_account = BankAccount.create()
your_account = BankAccount.create()
print(my_account.balance) # 0
print(BankAccount.total_funds()) # 0
my_account.deposit(200)
your_account.deposit(1000)
print(my_account.balance) # 200
print(your_account.balance) # 1000
print(BankAccount.total_funds()) # 1200
BankAccount.interest_time()
print(my_account.balance) # 202.0
print(your_account.balance) # 1010.0
print(BankAccount.total_funds()) # 1212.0
my_account.withdraw(50)
print(my_account.balance) # 152.0
print(BankAccount.total_funds()) # 1162.0