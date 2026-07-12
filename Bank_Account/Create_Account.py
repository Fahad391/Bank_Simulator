import random # Generates unique account numbers
from Account_Data_Manage import Manage_Account

# created a class Create_Account
class Create_Account:
    def __init__(self):
        self.account_num = ""
        self.name = ""
        self.age = 0
        self.account_type = ""
        self.initial_deposit_amount = 0
        self.pin_num = ""

    # Method to generate a unique account number
    def generate_account_number(self):
        unique_ID = random.randint(10000, 99999) # a range from 10000 to 99999
        self.account_num = f"BA--{unique_ID}"

    # Methods for input info

    # for name
    def input_name(self):
        # using While loop
        while True:
            name = input("Name: ").strip()

            # Cannot be empty
            if name == "":
                print("Name cannot be empty.\n")
                continue
            # Must contain letter or spaces or both
            if not all(ch.isalpha() or ch.isspace() for ch in name):
                print("Name can contain only letters and spaces.\n")
                continue
            # if everything alright
            self.name = name
            break
    
    # for age
    def input_age(self):
        while True:
            # using exception handling
            try:
                age = int(input("Age: "))
                
                # condition: age != 0 or age < 0
                if age <=0:
                    print("Age must be greater than 0.\n")
                    continue

                self.age = age
                break

            except ValueError:
                print("Please enter a valid age.\n")

    # for Account Type
    def Account_type(self):
        while True:
            print("\nAccount Type")

            if self.age < 18:
                print("1. Student")

                option = input("Enter Option: ")

                if option == "1":
                    self.account_type = "Student"
                    break

                print("Students below 18 can only create Student Accounts.\n")

            else:

                print("1. Savings")
                print("2. Current")
                print("3. Investment")

                option = input("Enter Option: ")

                if option == "1":
                    self.account_type = "Savings"
                    break
                elif option == "2":
                    self.account_type = "Current"
                    break

                elif option == "3":
                    self.account_type = "Investment"
                    break

                else:
                    print("Invalid Account Type. Try Again\n")

    # For Initial Deposit
    def initial_deposit(self):
        while True:
            try:
                amount = float(input("Initial Deposit (Minimum 100 BDT): "))

                if amount < 100:
                    print("Minimum deposit is 100 BDT.\n")
                    continue

                self.initial_deposit_amount = amount
                break

            except ValueError:
                print("Please enter a valid amount.\n")
    
    # for PIN
    def input_pin(self):

        while True:

            pin_num = input("Create 6-digit PIN: ")

            if pin_num == "": # Cannot be empty
                print("PIN cannot be empty.\n")
                continue

            if not pin_num.isdigit(): # Only digit
                print("PIN must contain only digits.\n")
                continue

            if len(pin_num) != 6: # Must be within 6 digit
                print("PIN must be exactly 6 digits.\n")
                continue

            self.pin_num = pin_num
            break


    # Method to Create Account
    def create_Account(self):
        print("Account Create Form")

        self.input_name()
        self.input_age()
        self.Account_type()
        self.initial_deposit()
        self.input_pin()
        self.generate_account_number()

        print("\n Account Created  ")
        print(f"Account Number: {self.account_num}")
        print(f"Name           : {self.name}")
        print(f"Age            : {self.age}")
        print(f"Account Type   : {self.account_type}")
        print(f"Deposit        : {self.initial_deposit_amount:.2f} BDT")
        print(f"PIN            : {self.pin_num}")

   
if __name__ == "__main__":
    account = Create_Account()
    account.create_Account()

    # Stores the inserted data in the database
    Store = Manage_Account()
    Store.insert_account(account)
    Store.close_connection()
