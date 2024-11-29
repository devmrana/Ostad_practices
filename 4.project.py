# Banking Management System
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        # Initialize a bank account object with the account holder's name and initial balance.
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        # Deposit a specified amount into the account.
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")

    def withdraw(self, amount):
        # Withdraw a specified amount from the account, if funds are available.
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        if amount > self.balance:
            print("Insufficient funds for this withdrawal.")
            return
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")

    def get_balance(self):
        # Return the current account balance.
        print(f"Current balance: ${self.balance:.2f}")
        return self.balance


def main():
    print("Welcome to the Banking Management System!")
    name = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance: "))
    account = BankAccount(name, initial_balance)

    while True:
        print("\nChoose an operation:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance Inquiry")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: $"))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: $"))
            account.withdraw(amount)
        elif choice == "3":
            account.get_balance()
        elif choice == "4":
            print("Thank you for using the Banking Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again. Select an option (1-4)")


if __name__ == "__main__":
    main()
