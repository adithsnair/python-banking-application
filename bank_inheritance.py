accounts=[]
account_number=1001
class BankAccount:
    def __init__(self, account_number, name, pin, balance):
        self.account_number = account_number
        self.name = name
        self.pin = pin
        self.balance = balance

    def deposit(self,amount):
        if amount<=0:
            print("Amount must be greater than 0")
        else:
            self.balance=self.balance+amount
            print("Deposit Successful")


class SavingsAccount(BankAccount):
    def withdraw(self,amount):
            if amount<=0:
                print("Amount must be greater than 0")
                return False
    
            elif self.balance<amount:
                print("Insufficient Balance")
                return False
    
            elif self.balance -amount<2000:
                print("Savings account must maintain a minimum balance of 2000")
                return False

            else:
                self.balance=self.balance-amount
                print("Withdrawal Successful")
                return True


class CurrentAccount(BankAccount):
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

def create_account(account_number):
    print("Create Account")
    print("1. Savings Account")
    print("2. Current Account")

    choice=int(input("Enter your choice:"))

    if choice ==1:
        name =input("Enter your name:")
        pin=input("Enter your PIN:")
        balance=float(input("Enter initial deposit:"))

        savings=SavingsAccount(account_number,name,pin,balance)
        accounts.append(savings)

        print("Savings Account Created")
        print("Your Account Number:",account_number)

        account_number+=1

    elif choice ==2:
        name=input("Enter your name:")
        pin=input("Enter your PIN:")
        balance=float(input("Enter initial deposit:"))

        current=CurrentAccount(account_number,name,pin,balance)
        accounts.append(current)

        print("Current Account Created")
        print("Your Account Number:",account_number)

        account_number+=1

    return account_number


def login(account_number):
    print("Login")

    if not accounts:
        print("No accounts found.Please create an account first.")
        return None

    login_account_number = int(input("Enter your Account Number: "))
    login_pin = input("Enter your PIN: ")

    for account in accounts:
        if account.account_number == login_account_number and account.pin == login_pin:
            print("Login Successful")
            print("Welcome", account.name)
            return account

    print("Invalid Credentials")
    return None


while True:
    print("Banking Application")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        account_number = create_account(account_number)

    elif choice == 2:
        account = login(account_number)

        if account is not None:
            while True:
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Logout")

                account_choice=int(input("Enter your choice:"))
                if account_choice == 1:
                    print("Account Balance:", account.balance)
                elif account_choice == 2:
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                elif account_choice == 3:
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                elif account_choice == 4:
                    print("Logged out")
                    break
                else:
                    print("Invalid Selection")

    elif choice == 3:
        print("Thank you!")
        break

    else:
        print("Invalid Selection")

