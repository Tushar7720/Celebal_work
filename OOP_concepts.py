class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} units. Current balance: {self.balance} units.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} units. Current balance: {self.balance} units.")

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance} units.")


# Creating bank account objects
account1 = BankAccount("123456789", "Tushar")
account2 = BankAccount("987654321", "Aniket", 1000)

# Depositing and withdrawing from account1
account1.display_account_info()
account1.deposit(500)
account1.withdraw(200)
account1.display_account_info()

# Depositing and withdrawing from account2
account2.display_account_info()
account2.deposit(1000)
account2.withdraw(500)
account2.display_account_info()
