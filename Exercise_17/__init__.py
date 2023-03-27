class Account:
    def __init__(self, account_number, balance, minimum_balance):
        self.account_number = account_number
        self.balance = balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            raise ValueError("Insufficient funds")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance


class PersonalAccount(Account):
    def __init__(self, account_number, balance, minimum_balance):
        super().__init__(account_number, balance, minimum_balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            raise ValueError("Insufficient funds")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance





