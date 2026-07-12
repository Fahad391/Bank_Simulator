import sqlite3

class Manage_Account:
    def __init__(self):
        self.connection = sqlite3.connect("Account_Data.db")
        self.cursor = self.connection.cursor()

        self.create_table()

    # Created a Method to Create Table
    def create_table(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Accounts(

            account_number TEXT PRIMARY KEY,

            name TEXT NOT NULL,

            age INTEGER NOT NULL,

            account_type TEXT NOT NULL,

            balance REAL NOT NULL,

            pin TEXT NOT NULL

        )
        """)

        self.connection.commit()

    # Created a method to insert data into that table
    def insert_account(self, account):
        try:

            self.cursor.execute("""
            INSERT INTO Accounts
            (
                account_number,
                name,
                age,
                account_type,
                balance,
                pin
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                account.account_num,
                account.name,
                account.age,
                account.account_type,
                account.initial_deposit_amount,
                account.pin_num
            ))

            self.connection.commit()

            print("Account Stored Successfully.")

        except sqlite3.Error as e:

            self.connection.rollback()

            print("Database Error:", e)

    # To Search a specific account
    def search_account(self, account_number):

        self.cursor.execute("""
        SELECT *
        FROM Accounts
        WHERE account_number = ?
        """, (account_number,))

        return self.cursor.fetchone()

    # To see all accounts
    def Display_all_accounts(self):

        self.cursor.execute("""
        SELECT *
        FROM Accounts
        """)

        return self.cursor.fetchall()
    
    # To count total accounts
    def total_accounts(self):

        self.cursor.execute("""
        SELECT COUNT(*)
        FROM Accounts
        """)

        return self.cursor.fetchone()[0]
    
    # To delete an Account
    def delete_account(self, account_number):

        self.cursor.execute("""
        DELETE FROM Accounts
        WHERE account_number = ?
        """, (account_number,))

        self.connection.commit()

        return self.cursor.rowcount
    
    # For updating balance
    def update_balance(self, account_number, new_balance):

        self.cursor.execute("""
        UPDATE Accounts
        SET balance = ?
        WHERE account_number = ?
        """,
        (new_balance, account_number))

        self.connection.commit()

    def close_connection(self):

     self.connection.close()

# Created object of the class
if __name__ == "__main__":
    admin = Manage_Account()

    # used while loop for input
    while True:
            print("  ADMIN MENU  ")
            print("1. Display All Accounts")
            print("2. Search Account")
            print("3. Count Accounts")
            print("4. Delete Account")
            print("5. Exit")

            command =input("Option: ")

            if command == "1":
                accounts = admin.Display_all_accounts()
                # used for loop to print in order
                for account in accounts:
                    print(account)
            elif command == "2":
                account_number = input("Enter Account Number: ")

                account = admin.search_account(account_number)

                if account:
                    print(account)
                else:
                    print("Account not found.")
            elif command == "3":
                print(f"Total Accounts: {admin.total_accounts()}")
            
            elif command == "4":
                account_number = input("Enter Account Number: ")
                deleted = admin.delete_account(account_number)

                if deleted:
                    print("Account deleted successfully.")
                else:
                    print("Account not found.")
            
            elif command == "5":

                admin.close_connection()
                break

            else:

                print("Invalid option.")