# Replica
# Admin⇒                                                                                                                             
# 1.Can create an account                                                                        
# 2.Can delete any user account                                                              
# 3.Can see all user accounts list                                                            
# 4.Can check the total available balance of the bank.                            
# 5.Can check the total loan amount.                                                       
# 6.Can on or off the loan feature of the bank.     

class BankAccount:
    accounts = []
    loan_amount = 0
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address      
        self.currenBalance = 0  
        self.transaction_history = [] 
        self.count_loan = 0

        BankAccount.accounts.append(self)

    def loan_taking(self, amount):
        if self.count_loan < 2:
            self.currenBalance += amount
            BankAccount.loan_amount += amount
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


class User:
    def __init__(self,name,email,password,address):
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.loan_feature = True

class Admin(User):
    def __init__(self,name,email,password,address):
        super().__init__(name,email,password,address)
        self.total_accounts = BankAccount.accounts

    
    def loan_feature_now(self):
        if self.loan_feature:
            self.loan_feature = False
            message = "---inactive----"
        else:
            self.loan_feature = True
            message = "-----active-------"
        print(f"Loan feature is now {message}")

    def total_loan_amount(self):
        total_loan =  BankAccount.loan_amount
        print(f"Total loan balance : {total_loan}")  
    
    def create_account(self, name, email, address):
        acc_new = BankAccount(name,email,address)
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
            print(f'Name is : {acc.name}, Email is : {acc.email}')



admin = Admin('Imon', 'imon@gmail.com','29','CU')
admin2 = Admin('ooImon', 'himon@gmail.com','29','CU')

currentUser = None

while(True):
    if currentUser == None:
        ch = input('\n login or Register? (L/R) : ')
        if ch == 'R':
            name = input('Enter your name : ')
            email = input('Enter your Email : ')
            password = input('Enter password : ')
            address = input('Enter adress : ')

            currentUser = Admin(name, email, password, address)
        
        else:
            email = input('Enter your Email : ')
            password = input('Enter password : ')

            for addmin in Admin.total_accounts:
                if email == addmin.email and password == addmin.password:
                    currentUser = addmin
                    break

    else:
        print()
        print(f'------ welcome {currentUser.name} ------')
        print()
        print('Chose Options')
        print('1.Creat Account')
        print('2.Delete Account')
        print('3.See all Account')
        print('5.total_loan_amount')
        print('6.loan feater now(ON/OFF)')
        print('7.Logout')
        print('')
        op = int(input('chose your options : '))
        if op == 1:
            new_name = input('Enter your name : ')
            new_email = input('Enter your Email : ')
            address = input('Enter address : ')
            new_acc = currentUser.create_account(new_name,new_email,address)

        elif op == 2:
            currentUser.delete_account(new_acc)

        elif op == 3:
            currentUser.see_all_accounts()

        elif op == 5:
            currentUser.total_loan_amount()

        elif op == 6:
            currentUser.loan_feature_now()

        elif op == 7:
            break

        else:
            print('------Invalid Option---------')
