# Lab 6: AI-Based Code Completion – Classes, Loops, and Conditionals
# File: ASS-6.3.py

# ============================================================================
# TASK 1: STUDENT CLASS
# ============================================================================

class Student:
    """A class to represent a student and manage their information."""
    
    def __init__(self, name, roll_number, branch):
        """Initialize student attributes."""
        self.name = name
        self.roll_number = roll_number
        self.branch = branch
    
    def display_details(self):
        """Display student information."""
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Branch: {self.branch}")

# Task 1 Execution
print("=" * 50)
print("TASK 1: STUDENT CLASS")
print("=" * 50)
student1 = Student("Harsha Vardhan", 101, "Computer Science")
student1.display_details()

# ============================================================================
# TASK 2: LOOPS (MULTIPLES OF A NUMBER)
# ============================================================================

def print_multiples_for(num, count=10):
    """Print first n multiples using for loop."""
    print(f"\nFirst {count} multiples of {num} (using for loop):")
    for i in range(1, count + 1):
        print(f"{num} × {i} = {num * i}", end="  ")
    print()

def print_multiples_while(num, count=10):
    """Print first n multiples using while loop."""
    print(f"\nFirst {count} multiples of {num} (using while loop):")
    i = 1
    while i <= count:
        print(f"{num} × {i} = {num * i}", end="  ")
        i += 1
    print()

# Task 2 Execution
print("\n" + "=" * 50)
print("TASK 2: LOOPS - MULTIPLES OF A NUMBER")
print("=" * 50)
print_multiples_for(5, 10)
print_multiples_while(7, 10)

# ============================================================================
# TASK 3: CONDITIONAL STATEMENTS (AGE CLASSIFICATION)
# ============================================================================

def classify_age_nested_if(age):
    """Classify age using nested if-elif-else statements."""
    if age < 0:
        return "Invalid age"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

def classify_age_dict(age):
    """Classify age using dictionary-based approach."""
    age_ranges = {
        (0, 13): "Child",
        (13, 20): "Teenager",
        (20, 60): "Adult",
        (60, 150): "Senior"
    }
    
    for (min_age, max_age), category in age_ranges.items():
        if min_age <= age < max_age:
            return category
    return "Invalid age"

# Task 3 Execution
print("\n" + "=" * 50)
print("TASK 3: CONDITIONAL STATEMENTS - AGE CLASSIFICATION")
print("=" * 50)
test_ages = [5, 15, 30, 70]
for age in test_ages:
    print(f"Age {age}: {classify_age_nested_if(age)}")

# ============================================================================
# TASK 4: FOR AND WHILE LOOPS (SUM OF FIRST N NUMBERS)
# ============================================================================

def sum_to_n_for(n):
    """Calculate sum of first n natural numbers using for loop."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_to_n_while(n):
    """Calculate sum of first n natural numbers using while loop."""
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

def sum_to_n_formula(n):
    """Calculate sum using mathematical formula: n(n+1)/2."""
    return n * (n + 1) // 2

# Task 4 Execution
print("\n" + "=" * 50)
print("TASK 4: FOR AND WHILE LOOPS - SUM OF FIRST N NUMBERS")
print("=" * 50)
test_n = 10
print(f"Sum of first {test_n} numbers (for loop): {sum_to_n_for(test_n)}")
print(f"Sum of first {test_n} numbers (while loop): {sum_to_n_while(test_n)}")
print(f"Sum of first {test_n} numbers (formula): {sum_to_n_formula(test_n)}")

# ============================================================================
# TASK 5: CLASSES (BANK ACCOUNT CLASS)
# ============================================================================

class BankAccount:
    """A class to represent a bank account with deposit and withdrawal operations."""
    
    def __init__(self, account_holder, initial_balance=0):
        """Initialize bank account with account holder name and balance."""
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"✓ Deposited: Rs. {amount}")
        else:
            print("✗ Invalid deposit amount")
    
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"✓ Withdrawn: Rs. {amount}")
        else:
            print("✗ Invalid withdrawal amount or insufficient balance")
    
    def check_balance(self):
        """Display the current account balance."""
        print(f"Account Balance: Rs. {self.balance}")

# Task 5 Execution
print("\n" + "=" * 50)
print("TASK 5: CLASSES - BANK ACCOUNT CLASS")
print("=" * 50)
account = BankAccount("Harsha Vardhan", 5000)
account.check_balance()
account.deposit(2000)
account.check_balance()
account.withdraw(1500)
account.check_balance()

print("\n" + "=" * 50)
print("ALL TASKS COMPLETED SUCCESSFULLY")
print("=" * 50)

