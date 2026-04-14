1
# 🔹 Function Implementation

def is_valid_username(username):
    
    # Check if input is string
    if not isinstance(username, str):
        return False

    # Length check
    if len(username) < 5 or len(username) > 15:
        return False
    
    # No spaces allowed
    if " " in username:
        return False
    
    # Must not start with digit
    if username[0].isdigit():
        return False
    
    # Only alphabets and digits
    if not username.isalnum():
        return False
    
    return True


# 🔹 Assert Test Cases (TDD Validation)

assert is_valid_username("User123") == True
assert is_valid_username("12User") == False
assert is_valid_username("Us er") == False
assert is_valid_username("User") == False
assert is_valid_username("U") == False
assert is_valid_username("User_123") == False
assert is_valid_username("ValidUser99") == True
assert is_valid_username("ThisUsernameIsTooLong123") == False

print(" Username validation logic successfully passing all test cases.")

2
#🔹 Assert Test Cases

#🔹 Function Implementation

def classify_value(x):
    # Check type using loop-style logic
    for _ in range(1):  # simple loop usage
        if not isinstance(x, int):
            return "Invalid Input"
        if x == 0:
            return "Zero"
        if x % 2 == 0:
            return "Even"
        else:
            return "Odd"
print("Value classification passed all tests")
assert classify_value(8) == "Even"
assert classify_value(7) == "Odd"
assert classify_value(0) == "Zero"
assert classify_value("abc") == "Invalid Input"
assert classify_value(15) == "Odd"

#3
import string
# Assert Test Cases
# Function Implementation
def is_palindrome(text):
    # Normalize string
    cleaned = ""
    for ch in text:
        if ch.isalnum():
            cleaned += ch.lower()
    # Check palindrome
    return cleaned == cleaned[::-1]
print("Palindrome tests passed successfully ")
assert is_palindrome("Madam") == True
assert is_palindrome("A man a plan a canal Panama") == True
assert is_palindrome("Python") == False
assert is_palindrome("") == True
assert is_palindrome("a") == True

4
#🔹 Class Implementation
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
    def get_balance(self):
        return self.balance
# 🔹 Assert Test Cases
acc = BankAccount(1000)
acc.deposit(500)
assert acc.get_balance() == 1500
acc.withdraw(300)
assert acc.get_balance() == 1200
acc.withdraw(2000)  # invalid withdrawal
assert acc.get_balance() == 1200
acc.deposit(-100)  # invalid deposit
assert acc.get_balance() == 1200
print("BankAccount class passed all tests ")

5
# 🔹 Function Implementation

def validate_email(email):
    # Must contain exactly one @
    if email.count("@") != 1:
        return False
    
    local, domain = email.split("@")
    
    # Local and domain must not be empty
    if not local or not domain:
        return False
    
    # Email must not start or end with special symbols
    if email[0] in "@._" or email[-1] in "@._":
        return False
    
    # Domain must contain at least one dot
    if "." not in domain:
        return False
    
    # Domain must not start or end with dot
    if domain.startswith(".") or domain.endswith("."):
        return False
    
    return True


# 🔹 Assert Test Cases

assert validate_email("user@example.com") == True
assert validate_email("userexample.com") == False
assert validate_email("@gmail.com") == False
assert validate_email("user@.com") == False
assert validate_email("user@domain.co") == True

print(" Email validation passed all tests ")
