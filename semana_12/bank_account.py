class BankAccount:
    def __init__(self, balance=0):
        # This is called when you create a new account
        self.balance = balance

    def deposit(self, amount):
        # Adds money to balance
        self.balance += amount

    def withdraw(self, amount):
        # Removes money from balance
        self.balance -= amount


class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        BankAccount.__init__(self, balance)  # Call parent class constructor
        self.min_balance = min_balance       # Set the minimum allowed balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print("Withdrawal denied: balance would go below minimum.")
        else:
            BankAccount.withdraw(self, amount)  # Call parent withdraw method
            print("Withdrawal successful. New balance:", self.balance)


git add . savings = SavingsAccount(200, 100)
print("Initial savings account balance:", savings.balance)

savings.withdraw(50)   # OK (200 → 150)
savings.withdraw(70)   # Denied (150 → 80 < 100)
savings.withdraw(20)   # OK (150 → 130)
