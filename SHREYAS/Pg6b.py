class InsufficientBalance(Exception):
    def __str__(self):
        return "Insufficient Balance"

class Account:
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self, amt):
        if amt < 0 :
            raise ValueError("Cannot deposit negative amount")
        self.balance += amt 
        print("Balance: ", self.balance)
    
    def withdraw(self, amt):
        if amt < 0 :
            raise ValueError("Cannot withdraw negative amount")
        if amt > self.balance:
            raise InsufficientBalance()
        self.balance -= amt 
        print("Balance: ", self.balance)

ac = Account(5000)
try:
        
    ac.deposit(50)
    # ac.deposit(-50)
    ac.withdraw(100)
    # ac.withdraw(-100)
    ac.withdraw(10000)
except Exception as ex:
    print(ex)
