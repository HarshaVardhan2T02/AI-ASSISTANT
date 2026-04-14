# Task 1: Username Validator
def is_valid_username(username):
    """Validates username based on requirements"""
    if not isinstance(username, str):
        return False
    if len(username) < 5 or len(username) > 15:
        return False
    if not username.replace('_', '').isalnum():
        return False
    if username[0].isdigit():
        return False
    if ' ' in username:
        return False
    return True

# Test cases for Task 1
assert is_valid_username("User123") == True
assert is_valid_username("12User") == False
assert is_valid_username("Us er") == False
assert is_valid_username("John") == False
assert is_valid_username("ValidUser99") == True

# Task 2: Even-Odd & Type Classification
def classify_value(x):
    """Classifies input as Even, Odd, Zero, or Invalid Input"""
    if isinstance(x, bool):
        return "Invalid Input"
    if isinstance(x, int):
        if x == 0:
            return "Zero"
        return "Even" if x % 2 == 0 else "Odd"
    return "Invalid Input"

# Test cases for Task 2
assert classify_value(8) == "Even"
assert classify_value(7) == "Odd"
assert classify_value("abc") == "Invalid Input"
assert classify_value(0) == "Zero"
assert classify_value(-4) == "Even"

# Task 3: Palindrome Checker
def is_palindrome(text):
    """Checks if text is palindrome, ignoring case, spaces, and punctuation"""
    if not isinstance(text, str):
        return False
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

# Test cases for Task 3
assert is_palindrome("Madam") == True
assert is_palindrome("A man a plan a canal Panama") == True
assert is_palindrome("Python") == False
assert is_palindrome("") == True
assert is_palindrome("a") == True

# Task 4: BankAccount Class
class BankAccount:
    """Bank account class with deposit, withdraw, and balance operations"""
    def __init__(self, initial_balance):
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.balance

# Test cases for Task 4
acc = BankAccount(1000)
acc.deposit(500)
assert acc.get_balance() == 1500
acc.withdraw(300)
assert acc.get_balance() == 1200
assert acc.withdraw(2000) == False

# Task 5: Email Validation
def validate_email(email):
    """Validates email format"""
    if not isinstance(email, str):
        return False
    if email.startswith('@') or email.startswith('.') or email.endswith('@') or email.endswith('.'):
        return False
    if '@' not in email or '.' not in email:
        return False
    parts = email.split('@')
    if len(parts) != 2 or not parts[0] or not parts[1]:
        return False
    if '.' not in parts[1]:
        return False
    return True

# Test cases for Task 5
assert validate_email("user@example.com") == True
assert validate_email("userexample.com") == False
assert validate_email("@gmail.com") == False
assert validate_email("user@domain") == False
assert validate_email("valid.user@example.co.uk") == True

print("All tests passed!")