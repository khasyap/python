class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print("Balance =", self.balance)

b = Bank(1000)

b.deposit(500)
b.show_balance()