# Bank Simulator (Python)

## Project Overview

This project is a console-based **Bank Simulator** built using Python. The purpose of this project was not only to create a working banking simulation, but also to strengthen my understanding of software design, Object-Oriented Programming (OOP), database integration, exception handling, and modular development.

Initially, the project included an ATM Simulator, but during development I decided to remove that module because its functionality overlapped with the Account Management and E-Wallet modules. Keeping the project focused resulted in a cleaner architecture.

The final project consists of three major modules:

* Bank Account Creation
* Account Management
* E-Wallet Transaction System

All modules share the same SQLite database and work together as one banking system.

---

# My Development Approach

Instead of starting with code, I first designed the system.

For every module, I followed the same process:

1. Identify the problem to solve.
2. Design the workflow.
3. Decide which file should own which responsibility.
4. Discuss and refine the design.
5. Implement the code.
6. Test, modify, and improve.

Throughout the project, I worked in a collaborative pair-programming style with ChatGPT. I was responsible for planning the system architecture, defining the business rules, making design decisions, testing the implementation, modifying code, adding comments, and identifying improvements. ChatGPT acted as a technical mentor by reviewing the design, suggesting better approaches, explaining concepts, writing initial implementations, and helping debug issues.

The final implementation is the result of this iterative design-and-review process.

---

# Project Structure

```text
Bank_Simulator/

│
├── Database/
│      └── Account_Data.db
│
├── Bank_Account/
│      ├── Create_Account.py
│      ├── Manage_Account.py
│      └── Account_Data_Manage.py
│
├── EWallet_Simulator/
│      ├── EWallet.py
│      └── Wallet_Exceptions.py
│
└── Main.py (Future Integration)
```

---

# Module 1: Create Account

## Purpose

Allows a customer to create a new bank account.

## Features

* Generates unique account numbers
* Name validation
* Age validation
* Account type selection
* Student account restriction for users under 18
* Minimum initial deposit validation
* Six-digit PIN creation
* Automatic database insertion

---

# Module 2: Account Management

## Purpose

Allows an existing customer to log in and manage their own account.

## Features

* Login using PIN
* View account details
* Deposit money
* Withdraw money
* Automatic database update
* Balance synchronization after every transaction

Only the logged-in user can access their own account information.

---

# Module 3: Admin Management

## Purpose

Provides administrative control over the database.

## Features

* View all accounts
* Search accounts
* Count total accounts
* Delete accounts
* Update balances
* Manage the banking database

This module is completely separate from the customer interface.

---

# Module 4: E-Wallet

## Purpose

Allows one customer to transfer money directly to another customer.

## Transaction Flow

Customer Login

↓

Enter Receiver Account

↓

Verify Receiver

↓

Enter Amount

↓

Validate Amount

↓

Check Available Balance

↓

Update Sender Balance

↓

Update Receiver Balance

↓

Commit Transaction

↓

Generate Receipt

---

## Receipt Includes

* Date and Time
* Sender Name
* Receiver Name
* Amount Sent
* Remaining Balance

---

# Database Design

SQLite was used to store all banking information.

Table:

Accounts

Fields:

* Account Number
* Name
* Age
* Account Type
* Balance
* PIN

Every module interacts with this single database.

---

# Object-Oriented Programming Concepts Used

## Encapsulation

Classes hide internal implementation and expose only the required methods.

Examples:

* Create_Account
* Manage_Account
* EWallet

---

## Abstraction

Users interact with simple commands such as:

* Create Account
* Deposit
* Withdraw
* Send Money

The SQL queries and internal logic remain hidden.

---

## Modularity

Every file has a single responsibility.

Create_Account.py

↓

Creates Accounts

Manage_Account.py

↓

Customer Operations

Account_Data_Manage.py

↓

Administrator Operations

EWallet.py

↓

Money Transfer

---

# Exception Handling

Custom exceptions were used to prevent the program from crashing.

Examples include:

* Invalid PIN
* Invalid PIN Format
* Invalid Amount
* Receiver Not Found
* Insufficient Balance

Input validation was applied throughout the project to handle invalid user input gracefully.

---

# Database Integration

SQLite is the central component of the project.

The project performs:

* INSERT
* SELECT
* UPDATE
* DELETE
* COMMIT
* ROLLBACK

The E-Wallet transaction updates both sender and receiver accounts within the same transaction to maintain database consistency.

---

# Software Engineering Lessons Learned

This project taught me that building software is not just about writing code.

The more important process is:

Think

↓

Design

↓

Discuss

↓

Refine

↓

Implement

↓

Test

↓

Refactor

↓

Document

I also learned that clear module boundaries make software easier to understand, maintain, and extend.


# Reflection

This project represents a significant milestone in my programming journey.

Rather than focusing only on syntax, I concentrated on understanding system design, software architecture, and modular programming. Building the simulator through iterative planning, implementation, testing, debugging, and refinement helped me appreciate how larger software systems are developed.

More importantly, this project changed the way I approach programming. I now begin by understanding the problem, defining responsibilities, designing the architecture, and only then writing code. That mindset is something I intend to carry into future software projects.
