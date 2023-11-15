# 1 . Can create an account with his/her name, email, address and account Type(Mainly Two Types: Savings & Cuurent).
class BankAccount:
    def __init__(self, name, email, address ,type):
        self.name = name
        self.email = email
        self.address = address
        self.type = type  
        self.accounts = []

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

