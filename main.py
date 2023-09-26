class BankAccount:
    # Initialize the attributes
    def __init__(self, account_number, account_holder_name, account_balance):
        # Make the attributes private by using double underscores
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = account_balance

    # Define a method to deposit money
    def deposit(self, amount):
        # Check if the amount is positive
        if amount > 0:
            # Add the amount to the account balance
            self.__account_balance += amount
            # Print a confirmation message
            print(f"Deposited {amount} to the account. New balance is {self.__account_balance}.")
        else:
            # Print an error message
            print("Invalid amount. Please enter a positive value.")

    # Define a method to withdraw money
    def withdraw(self, amount):
        # Check if the amount is positive and less than or equal to the account balance
        if amount > 0 and amount <= self.__account_balance:
            # Subtract the amount from the account balance
            self.__account_balance -= amount
            # Print a confirmation message
            print(f"Withdrew {amount} from the account. New balance is {self.__account_balance}.")
        else:
            # Print an error message
            print("Invalid amount. Please enter a positive value that is less than or equal to the current balance.")

    # Define a method to display the account balance
    def display_balance(self):
        # Print the account balance
        print(f"The current balance of the account is {self.__account_balance}.")

# Create an instance of the BankAccount class with some sample values
my_account = BankAccount(1234567890, "John Doe", 10000)

# Test the deposit and withdrawal functionality
my_account.deposit(5000) # Deposited 5000 to the account. New balance is 15000.
my_account.withdraw(3000) # Withdrew 3000 from the account. New balance is 12000.
my_account.display_balance() # The current balance of the account is 12000.
