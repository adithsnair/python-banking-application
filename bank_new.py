accounts=[]
class SavingsAccount:
    def __init__(self,name,pin,balance):
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
        elif self.balance<amount:
            print("Insufficient Balance")
        else:
            self.balance=self.balance-amount
            print("Withdrawal Successful")
                  
class CurrentAccount:
    def __init__(self,name,pin,balance):
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
        elif self.balance<amount:
            print("Insufficient Balance")
        else:
            self.balance=self.balance-amount
            print("Withdrawal Successful")

while True:
    print("Banking Application")
    print("1. Login")
    print("2. Create Account")
    print("3. Exit")

    choice=int(input("Enter Your Choice:"))
    if choice == 1:
        print("Login")
        print("1. Savings Account")
        print("2. Current Account")
        print("3. Exit")

        login_choice=int(input("Enter Your Choice:"))
        if login_choice == 1:
            print("Login to Savings Account")
            login_name=input("Enter your name:")
            login_pin=input("Enter your PIN:")

            logged_in = False

            for account in accounts:
                if isinstance(account, SavingsAccount) and login_name == account.name and login_pin == account.pin:
                    logged_in = True
                    print("Login Successful")
                    print("Welcome",account.name)
                    
                    while True:
                        print("1. Check Balance")
                        print("2. Deposit")
                        print("3. Withdraw")
                        print("4. Logout")
                        choice=int(input("Enter your choice:"))
                        if choice== 1:
                            print("Balance:",account.balance)
                        elif choice==2:
                            amount=int(input("Enter Deposit amount:"))
                            account.deposit(amount)
                        elif choice==3:
                            amount=int(input("Enter amount to be withdrawed"))
                            account.withdraw(amount)
                        elif choice==4:
                            print("Logged out")
                            break
                        else:
                            print("Invalid Selection")
            if not logged_in:
                print("Invalid Credentials")

        elif login_choice == 2:
            print("Login to Current Account")
            login_name = input("Enter your name: ")
            login_pin = input("Enter your PIN: ")

            logged_in=False

            for account in accounts:
                if isinstance(account, CurrentAccount) and login_name == account.name and login_pin == account.pin:
                    logged_in = True
                    print("Login Successful")
                    print("Welcome", account.name)

                    while True:
                        print("1.Check Balance")
                        print("2.Deposit")
                        print("3.Withdraw")
                        print("4.Logout")

                        choice=int(input("Enter your choice:"))
                        if choice == 1:
                            print("Balance:",account.balance)
                        elif choice == 2:
                            amount=int(input("Enter Deposit amount:"))
                            account.deposit(amount)
                        elif choice == 3:
                            amount=int(input("Enter amount to withdraw:"))
                            account.withdraw(amount)
                        elif choice == 4:
                            print("Logged out")
                            break
                        else:
                            print("Invalid Selection")
            if not logged_in:
                    print("Invalid Credentials")
                        
        else:
            print("Invalid Selection")

    elif choice == 2:
        print("Create Account")
        print("1. Savings Account")
        print("2. Current Account")

        create_choice=int(input("Enter Your Choice:"))
        if create_choice == 1:

            print("Create Savings Account")
            name=input("Enter your name:")
            pin=input("Enter your PIN:")
            balance=float(input("Enter initial deposit"))
            if balance<=0:
                print("Initial deposit must be greater than 0")
            else:
                savings=SavingsAccount(name, pin, balance)
                accounts.append(savings)
                print("Savings account Successfully Created")

        elif create_choice == 2:
            print("Create Current Account")
            name=input("Enter your name:")
            pin=input("Enter your PIN:")
            balance=float(input("Enter initial deposit"))
            if balance<=0:
                print("Initial deposit must be greater than 0")
            else:
                current=CurrentAccount(name,pin,balance)
                accounts.append(current)
                print("Current account Successfully created")
        else:
            print("Invalid Selection")

    elif choice ==3:
        print("Thank you !!")
        break
    else:
        print("Invalid Choice")
              