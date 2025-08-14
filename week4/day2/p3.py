# --- Custom Exceptions ---
class BankingError(Exception):
    pass

class InsufficientFundsError(BankingError):
    pass

class NegativeAmountError(BankingError):
    pass

class AccountNotFoundError(BankingError):
    pass

class InvalidAccountTypeError(BankingError):
    pass


# --- Bank Account Class ---
class BankAccount:
    def __init__(self, account_number, account_type, balance=0):
        valid_types = ["saving", "current"]
        if account_type.lower() not in valid_types:
            raise InvalidAccountTypeError(f"Invalid account type: {account_type}")
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise NegativeAmountError("Deposit amount must be positive.")
        self.balance += amount
        print(f"✅ Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise NegativeAmountError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError(f"Insufficient funds. Available balance: {self.balance}")
        self.balance -= amount
        print(f"✅ Withdrew {amount}. New balance: {self.balance}")

    def get_balance(self):
        print(f"💰 Current Balance: {self.balance}")


# --- Bank System Class ---
class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_type, balance=0):
        if account_number in self.accounts:
            raise BankingError("Account already exists.")
        self.accounts[account_number] = BankAccount(account_number, account_type, balance)
        print(f"✅ Account {account_number} created successfully.")

    def get_account(self, account_number):
        if account_number not in self.accounts:
            raise AccountNotFoundError(f"Account '{account_number}' does not exist.")
        return self.accounts[account_number]


# --- Main Program ---
bank = BankSystem()

while True:
    print("\n--- Banking System Menu ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            acc_num = input("Enter account number: ")
            acc_type = input("Enter account type (saving/current): ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(acc_num, acc_type, initial_balance)

        elif choice == "2":
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == "3":
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == "4":
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            account.get_balance()

        elif choice == "5":
            print(" Thank you for using our Banking System. Goodbye!")
            break

        else:
            print(" Invalid choice. Please try again.")

    except BankingError as e:
        print(f" Banking Error: {e}")
    except ValueError:
        print(" Invalid input. Please enter numbers where required.")
