# 6.Can take a loan from the bank at most two times.  
class BankAccount:
    def __init__(self, name, email, address ,type):
        self.name = name
        self.email = email
        self.address = address
        self.type = type  
        self.accounts = []     
        self.currenBalance = 0  
        self.transaction_history = [] 

        self.count_loan = 0

    def loan_taking(self, amount):
        if self.count_loan < 2:
            self.currenBalance += amount
            self.count_loan += 1
            self.transaction_history.append(f"Taking loan amount {amount}")
            print('----Taking loan Successfully-------')
        else:
            print('--Sorry . Maximum two time , you can take loan')


    def transaction_history_check(self):
        if self.transaction_history:
            print('----transaction History is showing:-----')
            for trans in self.transaction_history:
                print({trans})
        else:
            print('-----Yet, No transaction history is available------')


    def check_balance(self):
        print(f"Available balance is ${self.balance}")

    def deposit(self,amount):
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



account = BankAccount("imon", "imon@example.com", "chain St", "savings")

account.deposit(1000)
account.loan_taking(500)  # first loan
account.loan_taking(700)  # second loan
account.transaction_history_check()

account.loan_taking(200)  # limit cross
account.transaction_history_check()