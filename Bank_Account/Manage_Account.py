import sqlite3

class Manage_Account:
    def __init__(self):
        # Connect to the Data Base
        self.connection = sqlite3.connect('Account_Data.db')
        self.cursor = self.connection.cursor()

        self.current_account = None # No account is logged in

    # Created a Login method
    def Login(self):

        while True:
            pin = input("Enter PIN Number: ")

            # If empty
            if pin == "":
                print("PIN Number can't be empty\n")
                continue
            
            # If given letters
            if not pin.isdigit():
                print("PIN is only digit not letters")
                continue

            # Lenght cannot be under or over 6 digits
            if len(pin) != 6:
                print("PIN must be exactly 6 digits.\n")
                continue

            # Fetch the exact account logged in when PIN matched
            self.cursor.execute("""
                    SELECT *
                    FROM Accounts
                    WHERE pin = ?
                    """, (pin,))

            account = self.cursor.fetchone()

            if account:
                self.current_account = account
                print("\nLogin Successful.\n")
                return

            print("Wrong PIN.\n")

    # User can see their own account details
    def display_details(self):
        print("\n============ Account Details ============\n")
        print(f"Account Number : {self.current_account[0]}")
        print(f"Name           : {self.current_account[1]}")
        print(f"Age            : {self.current_account[2]}")
        print(f"Account Type   : {self.current_account[3]}")
        print(f"Balance        : {self.current_account[4]:.2f} BDT")

    
    # Created Deposit & Withdraw amount

    # Deposit
    def Deposit(self):

        while True:
            # using Exception Handling
            try:

                amount = float(input("Deposit Amount: "))
                # Amount cannot be negative
                if amount <0:
                    print("Amount cannot be a negative number\n ")
                    continue
                new_balance = self.current_account[4] + amount

                self.cursor.execute("""
                UPDATE Accounts
                SET balance = ?
                WHERE account_number = ?
                """,
                (new_balance, self.current_account[0]))

                self.connection.commit()

                print("Deposit Successful.")

                self.update_Account_Status()

                break

            except ValueError:
                print("Enter Valid amount\n")
            
    # Withdraw
    def Withdraw(self):
        while True:
            try:
                amount = float(input("Withdraw Amount: "))
                # amount cannot be negative
                if amount < 0:
                     print("Amount cannot be a negative number\n ")
                     continue
                if amount > self.current_account[4]:

                    print("Insufficient Balance.\n")
                    continue
            
                new_balance = self.current_account[4] - amount

                self.cursor.execute("""
                UPDATE Accounts
                SET balance = ?
                WHERE account_number = ?
                """,
                (new_balance, self.current_account[0]))

                self.connection.commit()

                print("Withdrawal Successful.")

                self.update_Account_Status()

                break

            except ValueError:

                print("Enter a valid amount.\n")
        
    # Update Account status after Withdraw/Deposit
    def update_Account_Status(self):
            self.cursor.execute("""
                SELECT *
                FROM Accounts
                WHERE account_number = ?
                """,
                (self.current_account[0],))

            self.current_account = self.cursor.fetchone() # only the logged in Account, not all

    # User Command Interface
    def command(self):
        self.Login()

        while True:
            print("\n User Command Interface \n")

            print("1. Account Details")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            command = input("Option: ")

            if command == "1":

                self.display_details()

            elif command == "2":

                self.Deposit()

            elif command == "3":

                self.Withdraw()

            elif command == "4":

                self.connection.close()

                print("Thank you.")

                break

            else:

                print("Invalid Option.")

# Create Object of the Class and Run
if __name__ == "__main__":
    customer = Manage_Account()
    customer.command()
    