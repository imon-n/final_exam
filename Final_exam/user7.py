# Can transfer the amount from his account to another user account. if the other account does not exist then show an error message “Account does not exist”.  
class BankAccount:
    accounts = []
    def __init__(self, name, email, address ,type):
        self.name = name
        self.email = email
        self.address = address
        self.type = type      
        self.currenBalance = 0  
        self.transaction_history = [] 
        self.count_loan = 0

        BankAccount.accounts.append(self)

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
        print(f"Available balance is ${self.currenBalance}")

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

    def transfer_amount(self, recipient_account, amount):
        if recipient_account in self.accounts:
            if amount <= self.currenBalance:
                self.currenBalance -= amount
                recipient_account.deposit(amount)
                self.transaction_history.append(f"Transferred ${amount} to {recipient_account.name}")
                print(f"Transferred ${amount} to {recipient_account.name}.")
            else:
                print("Insufficient balance.")
        else:
            print("Recipient account not found.")


account1 = BankAccount("Imon", "imon@gmail.com", "Chain", "savings")
account2 = BankAccount("Rana", "rana@gmail.com", "Savar", "savings")

account1.deposit(1000)  
account1.transfer_amount(account2, 500)  # Transfer from account 1 to account 2
# account2.check_balance()  # Check balance for account 2