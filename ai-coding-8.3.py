# ==============================
# Step 1: Test Cases (TDD First)
# ==============================

test_cases = [
    # Valid emails
    ("user@example.com", True),
    ("john.doe@gmail.com", True),
    ("test_user123@yahoo.co.in", True),
    ("a@b.co", True),

    # Invalid emails
    ("userexample.com", False),        # No @
    ("user@@example.com", False),      # Multiple @
    ("@example.com", False),           # No local part
    ("user@", False),                  # No domain
    ("user@com", False),               # No dot in domain
    ("user@.com", False),              # Domain starts with dot
    (".user@example.com", False),      # Starts with special char
    ("user@example.com.", False),      # Ends with special char
    ("user@exam ple.com", False),      # Space inside
    ("user@.com.", False),             # Starts/ends with special char
]


# ==============================
# Step 2: Implementation
# ==============================

def is_valid_email(email: str) -> bool:
    
    # No spaces allowed
    if " " in email:
        return False
    
    # Must contain exactly one '@'
    if email.count("@") != 1:
        return False
    
    local, domain = email.split("@")
    
    # Local and domain must not be empty
    if not local or not domain:
        return False
    
    # Must contain at least one '.' in domain
    if "." not in domain:
        return False
    
    # Must not start or end with special characters
    special_chars = ".@-_"
    
    if email[0] in special_chars or email[-1] in special_chars:
        return False
    
    # Domain should not start or end with '.'
    if domain.startswith(".") or domain.endswith("."):
        return False
    
    return True


# ==============================
# Step 3: Run Tests
# ==============================

print("Email Validation Test Results:\n")

all_passed = True

for email, expected in test_cases:
    result = is_valid_email(email)
    print(f"Email: {email} → Expected: {expected} → Actual: {result}")
    
    if result != expected:
        all_passed = False

print("\nAll Test Cases Passed!" if all_passed else "\nSome Test Cases Failed!")

# ==================================
# Step 1: Test Cases (TDD First)
# ==================================

# 2
test_cases = [
    # Valid Scores
    (95, "A"),
    (90, "A"),     # Boundary
    (89, "B"),
    (85, "B"),
    (80, "B"),     # Boundary
    (79, "C"),
    (75, "C"),
    (70, "C"),     # Boundary
    (69, "D"),
    (65, "D"),
    (60, "D"),     # Boundary
    (59, "F"),
    (40, "F"),
    (0, "F"),
    (100, "A"),

    # Invalid Inputs
    (-5, "Invalid Input"),
    (105, "Invalid Input"),
    ("eighty", "Invalid Input"),
]


# ==================================
# Step 2: Implementation
# ==================================

def assign_grade(score):
    
    # Check if input is numeric
    if not isinstance(score, (int, float)):
        return "Invalid Input"
    
    # Check range
    if score < 0 or score > 100:
        return "Invalid Input"
    
    # Grade assignment using loop over ranges
    grade_ranges = [
        (90, 100, "A"),
        (80, 89, "B"),
        (70, 79, "C"),
        (60, 69, "D"),
        (0, 59, "F")
    ]
    
    for lower, upper, grade in grade_ranges:
        if lower <= score <= upper:
            return grade


# ==================================
# Step 3: Run Tests
# ==================================

print("Grade Assignment Test Results:\n")

all_passed = True

for score, expected in test_cases:
    result = assign_grade(score)
    print(f"Score: {score} → Expected: {expected} → Actual: {result}")
    
    if result != expected:
        all_passed = False

print("\nAll Test Cases Passed!" if all_passed else "\nSome Test Cases Failed!")

# ==================================
# Step 1: Test Cases (TDD First)
# ==================================

# 3
test_cases = [
    # Palindromes
    ("A man a plan a canal Panama", True),
    ("Madam", True),
    ("No lemon, no melon", True),
    ("Was it a car or a cat I saw?", True),
    ("12321", True),
    ("", True),                      # Empty string
    ("!!!", True),                   # Only punctuation
    
    # Non-palindromes
    ("Hello World", False),
    ("OpenAI", False),
    ("Palindrome test", False),
    ("12345", False),
]


# ==================================
# Step 2: Implementation
# ==================================

def is_sentence_palindrome(sentence: str) -> bool:
    
    # Keep only alphanumeric characters and convert to lowercase
    cleaned = ""
    
    for ch in sentence:
        if ch.isalnum():
            cleaned += ch.lower()
    
    # Check if cleaned string is palindrome
    return cleaned == cleaned[::-1]


# ==================================
# Step 3: Run Tests
# ==================================

print("Sentence Palindrome Test Results:\n")

all_passed = True

for sentence, expected in test_cases:
    result = is_sentence_palindrome(sentence)
    print(f'Sentence: "{sentence}" → Expected: {expected} → Actual: {result}')
    
    if result != expected:
        all_passed = False

print("\nAll Test Cases Passed!" if all_passed else "\nSome Test Cases Failed!")

# 4
# ==================================
# Step 1: Test Scenarios (TDD First)
# ===================================

test_results = []

# ==================================
# Step 2: Implementation
# ==================================

class ShoppingCart:
    
    def __init__(self):
        self.items = {}   # Dictionary: {name: price}
    
    def add_item(self, name, price):
        if not isinstance(name, str) or not isinstance(price, (int, float)):
            return "Invalid Input"
        
        if price <= 0:
            return "Invalid Input"
        
        self.items[name] = price
        return "Item Added"
    
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            return "Item Removed"
        return "Item Not Found"
    
    def total_cost(self):
        total = 0
        for price in self.items.values():
            total += price
        return total


# ==================================
# Step 3: Test Cases Execution
# ==================================

print("ShoppingCart Test Results:\n")

cart = ShoppingCart()

# Test 1: Empty cart total
print("Test Empty Cart Total")
print("Expected: 0 → Actual:", cart.total_cost(), "\n")

# Test 2: Add single item
print("Test Add Single Item")
cart.add_item("Laptop", 50000)
print("Expected: 50000 → Actual:", cart.total_cost(), "\n")

# Test 3: Add multiple items
print("Test Add Multiple Items")
cart.add_item("Mouse", 1000)
cart.add_item("Keyboard", 2000)
print("Expected: 53000 → Actual:", cart.total_cost(), "\n")

# Test 4: Remove item
print("Test Remove Item")
cart.remove_item("Mouse")
print("Expected: 52000 → Actual:", cart.total_cost(), "\n")

# Test 5: Remove non-existing item
print("Test Remove Non-existing Item")
result = cart.remove_item("Tablet")
print("Expected: Item Not Found → Actual:", result, "\n")

# Test 6: Invalid price
print("Test Invalid Price")
result = cart.add_item("Tablet", -500)
print("Expected: Invalid Input → Actual:", result, "\n")

print("All tests executed successfully.")

#5
# ==================================
# Step 1: Test Cases (TDD First)
# ==================================

test_cases = [
    # Valid Dates
    ("2023-10-15", "15-10-2023"),
    ("2023-01-01", "01-01-2023"),
    ("1999-12-31", "31-12-1999"),
    ("2024-02-29", "29-02-2024"),  # Leap year
    
    # Invalid Formats
    ("15-10-2023", "Invalid Date Format"),
    ("2023/10/15", "Invalid Date Format"),
    ("2023-13-01", "Invalid Date Format"),  # Invalid month
    ("2023-00-10", "Invalid Date Format"),  # Invalid month
    ("2023-02-30", "Invalid Date Format"),  # Invalid day
    ("abcd-ef-gh", "Invalid Date Format"),
    ("", "Invalid Date Format"),
]


# ==================================
# Step 2: Implementation
# ==================================

from datetime import datetime

def convert_date_format(date_str: str) -> str:
    try:
        # Parse input date
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        
        # Convert to required format
        return date_obj.strftime("%d-%m-%Y")
    
    except (ValueError, TypeError):
        return "Invalid Date Format"


# ==================================
# Step 3: Run Tests
# ==================================

print("Date Format Conversion Test Results:\n")

all_passed = True

for date_input, expected in test_cases:
    result = convert_date_format(date_input)
    print(f"Input: {date_input} → Expected: {expected} → Actual: {result}")
    
    if result != expected:
        all_passed = False

print("\nAll Test Cases Passed!" if all_passed else "\nSome Test Cases Failed!")

#write code for 