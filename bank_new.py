accounts=[]
account_number=1001
class SavingsAccount:
    def __init__(self,account_number,name,pin,balance):
        self.account_number=account_number
        self.name=name
        self.pin=pin
        self.balance=balance


    def deposit(self,amount):
        if amount<=0:
            print("Amount must be greater than 0")
        else:
            self.balance=self.balance+amount
            print("Deposit Successful")

    def withdraw(self,amount):
        if amount<=0:
            print("Amount must be greater than 0")
            return False
        elif self.balance<amount:
            print("Insufficient Balance")
            return False
        elif self.balance -amount<2000:
            print("Savings Account must maintain a minimum balance of 2000")
            return False
        else:
            self.balance=self.balance-amount
            print("Withdrawal Successful")
            return True

                  
class CurrentAccount:
    def __init__(self,account_number,name,pin,balance):
        self.account_number=account_number
        self.name=name
        self.pin=pin
        self.balance=balance

    def deposit(self,amount):
        if amount<=0:
            print("Amount must be greater than 0")
        else:
            self.balance=self.balance+amount
            print("Deposit Successful")

    def withdraw(self,amount):
        if amount<=0:
            print("Amount must be greater than 0")
            return False
        elif amount>self.balance+5000:
            print("Overdraft limit exceeded")
            return False
        else:
            self.balance=self.balance-amount
            print("Withdrawal Successful")
            return True

def login(account_number):
    print("Login")

    if not accounts:
       print("No accounts found. Please create an account first.")
       account_number = create_account(account_number)
       return account_number
    
    login_account_number = int(input("Enter your Account Number: "))
    login_pin = input("Enter your PIN: ")

    logged_in = False

    for account in accounts:
        if account.account_number == login_account_number and account.pin == login_pin:
            print("Login Successful")
            print("Welcome", account.name)

            logged_in = True

            while True:
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Logout")
                choice=int(input("Enter your choice:"))
                if choice== 1:
                       print("Balance:",account.balance)
                elif choice==2:
                    while True:
                        amount=int(input("Enter Deposit amount:"))
                        if amount<=0:
                            print("Amount must be greater than 0")
                        else:
                            account.deposit(amount)
                            break
                elif choice==3:
                    while True:
                        amount=int(input("Enter amount to be withdrawed"))                        
                        if account.withdraw(amount):
                            break
                elif choice==4:
                    print("Logged out")
                    break
                else:
                    print("Invalid Selection")
            return account_number

    if not logged_in:
        print("Invalid Credentials")
        return account_number


def create_account(account_number):
    print("Create Account")
    print("1. Savings Account") 
    print("2. Current Account")

    create_choice=int(input("Enter your choice:"))

    if create_choice == 1:
        print("Create Savings Account")
        name=input("Enter your name:")
        pin=input("Enter your PIN:")
        balance=float(input("Enter initial deposit"))
        if balance<=0:
             print("Initial deposit must be greater than 0")
        else:
             savings=SavingsAccount(account_number,name, pin, balance)
             accounts.append(savings)
             print("Savings Account Successfully Created")
             print("Your Account Number:", account_number)
             account_number += 1

    elif create_choice == 2:
        print("Create Current Account")
        name=input("Enter your name:")
        pin=input("Enter your PIN:")
        balance=float(input("Enter initial deposit"))

        if balance<=0:
            print("Initial deposit must be greater than 0")
        else:
            current=CurrentAccount(account_number,name,pin,balance)
            accounts.append(current)
            print("Current Account Successfully Created")
            print("Your Account Number:",account_number)
            account_number += 1
    return account_number   


while True:
    print("Banking Application")
    print("1. Login")
    print("2. Create Account")
    print("3. Exit")

    choice=int(input("Enter Your Choice:"))
    if choice == 1:
        account_number = login(account_number)
    elif choice==2:
            account_number = create_account(account_number)
    elif choice==3:
        print("Thank you !!")
        break
    else:
        print("Invalid Selection")