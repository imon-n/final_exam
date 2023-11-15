# 3.Can deposit and withdraw amount. If the withdrawal amount is more than the current balance, show an error message that “Withdrawal amount exceeded”

class BankAccount:
    def __init__(self, name, email, address ,type):
        self.name = name
        self.email = email
        self.address = address
        self.type = type  
        self.accounts = []

        self.currenBalance = 0  
        self.account_number = self.account_number()

    def deposite(self,amount):
        if amount >=0 :
            self.currenBalance += amount
        else:
            print('\n Withdrawal amount exceeded \n')

    def withdraw(self,amount):
        if amount >= 0 and amount <= self.currenBalance:
            self.currenBalance -= amount
        else:
            print('\n Withdrawal amount exceeded \n')

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

