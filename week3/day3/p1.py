class Bank_account:
    def __init__(self):
        self.balance=0
        print("Hello!welcome to Deposit and Withdrawal")

    def deposit(self):
        amount=float(input("Enter amount to be Deposit"))
        self.balance +=amount
        print("\n Amount Deposit",amount)
    
    def withdraw(self):
        amount=float(input("enter amount to withdrawal"))
        if self.balance>=amount:
            self.balance-=amount
            print(f"you withdraw",amount)
        else:
            print("insufficient balance")
    def display(self):
        print("\n Now Available balance",self.balance)

s=Bank_account()
s.deposit()
s.withdraw()
s.display()