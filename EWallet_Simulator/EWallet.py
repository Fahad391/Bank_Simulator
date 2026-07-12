import sqlite3
from Project_exception import *
from datetime import datetime

class EWallet:
    def __init__(self):
        self.connection = sqlite3.connect("Account_Data.db")
        self.cursor = self.connection.cursor()
        
        self.current_account = None      # No user is logged in
        self.last_transaction = None     # No transaction has occurred

    # Created Login Method
    def Login(self):
        while True:
             try:
                pin = input("Enter PIN Number: ")

                # If PIN is empty
                if pin == "":
                    raise InvalidPIN("PIN can't be empty")
                
                # If user inputs letter
                if not pin.isdigit():
                    raise InvalidPINFormat("PIN must contain only digits.")
                
                # PIN not less or more than 6 Digits
                if len(pin) != 6:
                    raise InvalidPINFormat("PIN must be exactly 6 digits.")

                # Search account
                self.cursor.execute("""
                            SELECT *
                            FROM Accounts
                            WHERE pin = ?
                        """, (pin,))

                account = self.cursor.fetchone() # Fetch the found account

                if account is None:
                    raise InvalidPIN("Wrong PIN.")
                
                self.current_account = account 
                break
        
             except (InvalidPIN, InvalidPINFormat ) as error:
                print("Error: ", error)

    # Created Transaction Method
    def Transaction(self):
        while True:
            try:
                # Whom we gonna send money
                receiver_account = input("Receiver Account Number: ")
                 # Search if the Receiver account actually exist or not
                self.cursor.execute("""
                    SELECT *
                    FROM Accounts
                    WHERE account_number = ?
                """, (receiver_account,))

                receiver = self.cursor.fetchone()

                # Receiver doesn't exist
                if receiver is None:
                    raise ReceiverNotFound("Receiver account not found.")

                # Prevent sending money to own account
                if receiver[0] == self.current_account[0]:
                  raise SameAccountTransfer("You cannot send money to your own account.")

                # Amount to send
                amount = float(input("Amount to Send: "))

                # Amount cannot be negative
                if amount <= 0:
                    raise InvalidAmount("Amount must be greater than 0.")

                # Sender balance
                sender_balance = self.current_account[4]

                # Receiver balance
                receiver_balance = receiver[4]

                # Insufficient balance
                if amount > sender_balance:
                    raise InsufficientBalance("Insufficient Balance.")

                # Calculate balances
                new_sender_balance = sender_balance - amount
                new_receiver_balance = receiver_balance + amount

                # Update Sender's & Receiver's Account Balance
                
                #Sender
                self.cursor.execute("""
                UPDATE Accounts
                SET balance = ?
                WHERE account_number = ?
            """,
            (new_sender_balance, self.current_account[0]))

           # Receiver
                self.cursor.execute("""
                UPDATE Accounts
                SET balance = ?
                WHERE account_number = ?
            """,
            (new_receiver_balance, receiver_account))
                
            # Save both updates
                self.connection.commit()

             # Update current logged-in account
                current = list(self.current_account)
                current[4] = new_sender_balance
                self.current_account = tuple(current)

                print("\n========== TRANSACTION RECEIPT ==========\n")

                print(f"Date              : {datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}")
                print(f"Sender            : {self.current_account[1]}")
                print(f"Amount Sent       : {amount:.2f} BDT")
                print(f"Receiver          : {receiver[1]}")
                print(f"Remaining Balance : {new_sender_balance:.2f} BDT")

                print("\nTransaction Successful.\n")

                break

            except (ReceiverNotFound,InvalidAmount,InsufficientBalance) as error:
                    print("Error: ", error)
            except ValueError:
                print("Enter a valid amount.\n")
            except sqlite3.Error as e:
                self.connection.rollback()
                print("Database Error:", e)

    # User Command Interface
    def Command(self):

        # Have to Login first
        self.Login()

        while True:

            print("\n      E-Wallet    \n")

            print("1. Send Money")
            print("2. Exit")

            command = input("Option: ")

            if command == "1":

                self.Transaction()

            elif command == "2":
                self.connection.close()
                print("\nLogged Out")
                break
            else:
                print("Invalid Option.\n")


# Create Object of the Class and Run
if __name__ == "__main__":

    wallet = EWallet()
    wallet.Command()
