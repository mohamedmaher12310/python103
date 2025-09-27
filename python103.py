import datetime

class BankAccount:
    def __init__(self,account_number,account_name,balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self,account_number,amount):
        self.account_number=account_number
        if amount>0:
            self.balance+=amount
            date = datetime.datetime.now()
            print(f"new amount added to your balance of {amount}\n ")
            print(f" Date: {date}")
        else:
            print("The deposited amount must be positive\n")


    def withdraw(self,amount):
        if amount>0:
            date = datetime.datetime.now()
            print(f"new amount withdrawn from your balance of {amount}\n ")
            print(f" Date: {date}")
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("the transaction refused, your balance smaller than this needed amount\n")
        else:
            print("amount must be positive\n")


    def current_balance(self):
        print(f"Your current balance is {self.balance}")


class Bank:
    def __init__(self):
        self.accounts={}


    def create_account(self,account_number,holder_name,initial_deposite=0):
        if account_number in self.accounts:
            print("Account number already exists.Please use different number")
        else:
            self.accounts[account_number]=BankAccount(account_number,holder_name,initial_deposite)
            print(f"Account {account_number} created for {holder_name} with balance ${initial_deposite}")



my_bank =Bank()

my_bank.create_account(123,"Mohamed")
my_bank.create_account(456,"ahmed")

person1 = BankAccount(123,"Mohamed")
person1.current_balance()
person1.deposit(123,5000)
person1.current_balance()
person1.withdraw(750)
person1.current_balance()