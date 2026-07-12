# If there's given a Wrong PIN 
class InvalidPIN(Exception):
    pass


# If PIN contains letters
class InvalidPINFormat(Exception):
    pass


# If Amount is negative or Zero
class InvalidAmount(Exception):
    pass


#If Receiver account doesn't exist
class ReceiverNotFound(Exception):
    pass


# Sender doesn't have enough money to send
class InsufficientBalance(Exception):
    pass

# If try to send money into own account
class SameAccountTransfer(Exception):
    pass