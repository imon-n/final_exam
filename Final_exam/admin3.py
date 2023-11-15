# Admin⇒                                                                                                                             
# 1.Can create an account                                                                        
# 2.Can delete any user account                                                              
# 3.Can see all user accounts list  


class User:
    def __init__(self,name,email,password,address):
        self.name = name
        self.email = email
        self.password = password
        self.address = address

class Admin(User):
    def __init__(self,name,email,password,address):
        super().__init__(name,email,password,address)
        self.total_accounts = BankAccount.accounts
    
    def create_account(self, name, email, address ,type):
        acc_new = BankAccount(name,email,address,type)
        # self.total_accounts.append(acc_new)
        return acc_new

    def delete_account(self,account):
        if account in self.total_accounts:
            self.total_accounts.remove(account)
            del account
            print('-----Successfull to delete account-------')
        else:
            print('---Account is unavailable or not found----')


    # 3.Can see all user accounts list  
    # 3.Can see all user accounts list  
    def see_all_accounts(self):
        for acc in BankAccount.accounts:
            print(f"Name: {acc.name}, Email: {acc.email}, Type: {acc.type}")


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





admin = Admin('Imon', 'imon@gmail.com','29','CU')

acc1 = admin.create_account('joni', 'jono@gmail.com','Dhaka','savings')
acc2 = admin.create_account('000000joni', 'hhhh@gmail.com','kU','savings')

admin.see_all_accounts()
admin.delete_account(acc1)
admin.see_all_accounts()

