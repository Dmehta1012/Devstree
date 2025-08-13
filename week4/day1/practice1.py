import os

class Account:
    def __init__(self, bal, acc_no, filename="Account_details.txt"):
        self.account_no = acc_no
        self.file_name = filename

        if os.path.exists(self.file_name):  # Load saved data if file exists
            with open(self.file_name, "r") as f:
                lines = f.readlines()
                self.account_no = int(lines[0].split(":")[1].strip())
                self.balance = int(lines[1].split(":")[1].strip())
        else:
            self.balance = bal
            self.save_to_file()

    def save_to_file(self):
        with open(self.file_name, "w") as f:
            f.write(f"Account No: {self.account_no}\n")
            f.write(f"Balance: {self.balance}\n")

    def read_file(self):
        with open(self.file_name, "r") as f:
            print("\n--- File Content ---")
            print(f.read())

    def choice(self):
        while True:
            print("\nEnter choice what you want to do\n"
                  "1. Check Balance\n"
                  "2. Credit Amount\n"
                  "3. Debit Amount\n"
                  "4. View File Data\n"
                  "5. Exit\n")
            choice = int(input("Enter number between (1-5): "))

            if choice == 1:
                print(f"Your Balance is {self.get_balance()}")

            elif choice == 2:
                c = int(input("Enter Amount to credit in account: "))
                self.balance += c
                print(f"Rs {c} is credited")
                print(f"Total Balance: {self.get_balance()}")
                self.save_to_file()

            elif choice == 3:
                amount = int(input("Enter amount to debit from account: "))
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Rs {amount} was debited")
                else:
                    print("Insufficient balance")
                print(f"Total Balance: {self.get_balance()}")
                self.save_to_file()

            elif choice == 4:
                self.read_file()

            elif choice == 5:
                print("Thanks for visiting")
                break

            else:
                print("Invalid Input")

    def get_balance(self):
        return self.balance


# Start the program — loads old balance if file exists
a = Account(10000, 14656154)
a.choice()
