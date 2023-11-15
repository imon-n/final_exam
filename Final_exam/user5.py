# 5.Can check transaction history.

class BankAccount:
    def __init__(self, name, email, address ,type):
        self.name = name
        self.email = email
        self.address = address
        self.type = type  
        self.accounts = []

        self.currenBalance = 0  
        self.transaction_history = [] 

    
    def transaction_history_check(self):
        if self.transaction_history:
            print('----transaction History is showing:-----')
            for trans in self.transaction_history:
                print({trans})
        else:
            print('-----Yet, No transaction history is available------')



    def check_balance(self):
        print(f"Available balance is ${self.currenBalance}")

    def deposite(self,amount):
        if amount >=0 :
            self.currenBalance += amount
            self.transaction_history.append(f'Deposited money {amount}')
        else:
            print('\n Withdrawal amount exceeded \n')

    def withdraw(self,amount):
        if amount >= 0 and amount <= self.currenBalance:
            self.currenBalance -= amount
            self.transaction_history.append(f'Withdrew money {amount}')
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


account = BankAccount("imon", "imon@example.com", "chain St", "savings")

account.deposite(1000)
account.check_balance()
account.withdraw(700)
account.check_balance()
account.transaction_history_check()
