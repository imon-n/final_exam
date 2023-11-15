# 4.Can check available balance.    

class BankAccount:
    def __init__(self, name, email, address ,type):
        self.name = name
        self.email = email
        self.address = address
        self.type = type  
        self.accounts = []

        self.balance = 0  # Setting initial balance to 0
        self.account_number = self.account_number()

    def check_balance(self):
        print(f"Available balance is ${self.balance}")

class Savings(BankAccount):
    def __init__(self, name, email, address):
        super().__init__(name, email, address,'saving')

class CurrentAccount(BankAccount):
    def __init__(self, name, email, address, type):
        super().__init__(name, email, address,'current_account')

class User:
    def __init__(self, name,email, password,address):
        self.name = name
        self.email = email
        self.address = password
        self.address = address



        
