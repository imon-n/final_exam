# Replica
# Replica (for user/admin)
class BankAccount:
    accounts = []
    loan_amount = 0
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address      
        self.currenBalance = 0  
        self.transaction_history = [] 
        self.count_loan_cont = 0
        self.total_loan_amount = 0

        BankAccount.accounts.append(self)

    def loan_taking(self, amount):
        if self.count_loan_cont < 2 and amount < self.currenBalance:
            self.currenBalance -= amount
            self.count_loan_cont += 1
            self.total_loan_amount += amount
            self.transaction_history.append(f"Taking loan amount {amount}")

            print(f" Total amount Loan is  :{self.total_loan_amount} taken.")
        else:
            print(f"-----Sorry----Loan of taken..")


    def transaction_history_check(self):
        if self.transaction_history:
            print('----transaction History is showing:-----')
            for trans in self.transaction_history:
                print({trans})
        else:
            print('-----Yet, No transaction history is available------')


    def check_balance(self):
        print(f"Available balance is : {self.currenBalance}")

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



    def see_all_accounts(self):
        for acc in BankAccount.accounts:
            print(f'Name is : {acc.name}, Email is : {acc.email}')



admin = Admin('imon', 'imon@','29','CU')

user = BankAccount("imon", "imon@", "chain St")

currentAdmin = None
currentUser = None

op = input('\n User/Admin -----? (ad/us) : ')

while True:
    if op == 'us':
        if currentUser == None:
            ch = input('\n login or Register(user)? (L/R) : ')
            if ch == 'R':
                name = input('Enter your name : ')
                email = input('Enter your Email : ')
                address = input('Enter adress : ')
                currentUser = BankAccount(name, email, address)
        
            else:
                email = input('Enter your Email : ')
                if email == user.email:
                    currentUser = user
                        
        else:
            print()
            print(f'------ welcome {currentUser.name} ------')

            print('1. Check Balance')
            print('2. Deposit Money')
            print('3. Withdraw Money')
            print('5. Take Loan')
            print('6. View Transaction History')  
            print('7. logOut')

            choice = input('\nEnter your choice: ')

            if choice == '7':
                currentUser = None
                print('Logged out successfully.')

            elif choice == '1':
                currentUser.check_balance()

            elif choice == '2':
                amount = int(input('Enter the amount to deposit: '))
                currentUser.deposit(amount)
                print('Deposit successful.')

            elif choice == '3':
                amount = int(input('Enter the amount to withdraw: '))
                currentUser.withdraw(amount)
                print('Withdrawal successful.')

            elif choice == '5':
                amount = int(input('Enter the loan amount: '))
                currentUser.loan_taking(amount)

            elif choice == '6':
                currentUser.transaction_history_check()

    else:
        if currentAdmin == None:
            ch = input('\n login or Register(Adimn) ? (L/R) : ')
            if ch == 'R':
                name = input('Enter your name : ')
                email = input('Enter your Email : ')
                password = input('Enter password : ')
                address = input('Enter adress : ')

                currentAdmin = Admin(name, email, password, address)
        
            else:
                email = input('Enter your Email : ')
                password = input('Enter password : ')

                if email == admin.email and password == admin.password:
                    currentAdmin = addmin
                else:
                    print('--Wrong email/password,\n please, try again---')

        else:
            print()
            print(f'------ welcome {currentAdmin.name} ------')
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
                new_acc = currentAdmin.create_account(new_name,new_email,address)

            elif op == 2:
                currentAdmin.delete_account(new_acc)

            elif op == 3:
                currentAdmin.see_all_accounts()

            elif op == 5:
                currentAdmin.total_loan_amount()

            elif op == 6:
                currentAdmin.loan_feature_now()

            elif op == 7:
                currentAdmin = None
                print('Logged out successfully.')

            else:
                print('------Invalid Option---------')