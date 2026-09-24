accounts=[]

class BankAccount:
    def __init__(self,name,pin,balance):
        self.name=name
        self.pin=pin
        self.balance=balance

    def deposit(self,amount):
        if amount <= 0:
            print("Amount must be greater than 0")
        else:
            self.balance=self.balance+amount
            print("Deposit Successful")

    def withdraw(self,amount):
        if amount <= 0:
            print("Amount must be greater than 0")
        elif amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance=self.balance-amount
            print("Withdrawal Successful")

while True:
    print("Banking Application")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice=int(input("Enter your choice:"))

    if choice == 1:
        print("Create Account")                                                                                                                                         

        name=input("Enter your name:")
        pin=input("Enter PIN:")

        while True:
            balance=float(input("Enter Deposit amount:"))

            if balance > 0:
                break
            else:
                print("Amount must be greater than 0")


        account=BankAccount(name,pin,balance)
        accounts.append(account)

    elif choice == 2:
        print("Login")

        login_name=input("Enter your name:")
        login_pin=input("Enter PIN:")

        logged_in = False

        for account in accounts:
            if login_name == account.name and login_pin == account.pin:
                logged_in = True
                print("Login Successful")
                print("Welcome",account.name)

                while True:
                    print("1. Account Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Logout")

                    account_choice=int(input("Enter your choice:"))

                    if account_choice == 1:
                        print("Account Balance:",account.balance)
                    elif account_choice == 2:
                        account_deposit = float(input("Enter the deposit amount:"))
                        account.deposit(account_deposit)
                    elif account_choice == 3:
                        account_withdraw = float(input("Enter withdraw amount:"))
                        account.withdraw(account_withdraw)
                    elif account_choice == 4:
                        print("Logged out")
                        break
                    else:
                        print("Invalid selection")

                break

        if not logged_in:
            print("Invalid Credentials")

    elif choice == 3:
        print("Thank you!!")
        break
    else:
        print("Invalid Choice")
            
