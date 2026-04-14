import time

# Lab 13: Code Refactoring – Improving Legacy Code with AI

# ============================================================================
# TASK 1: Removing Global Variables
# ============================================================================

# Refactored: Pass rate as parameter
def calculate_interest(amount, rate=0.1):
    """Calculate interest with rate passed as parameter."""
    return amount * rate

print("Task 1 - Interest Calculation:")
print(calculate_interest(1000))  # Output: 100.0
print()

# ============================================================================
# TASK 2: Refactoring Deeply Nested Conditionals
# ============================================================================

# Refactored: Using a mapping-based approach
def get_grade(score):
    """Determine grade using guard clauses."""
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Very Good"
    elif score >= 60:
        return "Good"
    else:
        return "Needs Improvement"

print("Task 2 - Grade Classification:")
score = 78
print(get_grade(score))  # Output: Very Good
print()

# ============================================================================
# TASK 3: Refactoring Repeated File Handling Code
# ============================================================================

def read_file(filename):
    """Read and return file contents using context manager."""
    with open(filename, 'r') as f:
        return f.read()

def read_multiple_files(filenames):
    """Read multiple files efficiently."""
    results = []
    for filename in filenames:
        try:
            results.append((filename, read_file(filename)))
        except FileNotFoundError:
            print(f"Warning: {filename} not found")
    return results

print("Task 3 - File Handling (requires files):")
# Uncomment if files exist:
# print(read_file("data1.txt"))
# print(read_file("data2.txt"))
print()

# ============================================================================
# TASK 4: Optimizing Search Logic
# ============================================================================

def check_access(username, users):
    """Check access using set for O(1) lookup instead of O(n)."""
    user_set = set(users)
    return "Access Granted" if username in user_set else "Access Denied"

print("Task 4 - User Access Optimization:")
users = ["admin", "guest", "editor", "viewer"]
# name = input("Enter username: ")  # Uncomment for interactive input
name = "admin"
print(check_access(name, users))  # Output: Access Granted
print()

# ============================================================================
# TASK 5: Refactoring Procedural Code into OOP Design
# ============================================================================

class EmployeeSalaryCalculator:
    """Calculate employee salary and deductions."""
    
    def __init__(self, salary, tax_rate=0.2):
        self.salary = salary
        self.tax_rate = tax_rate
    
    def calculate_tax(self):
        """Calculate tax amount."""
        return self.salary * self.tax_rate
    
    def calculate_net_salary(self):
        """Calculate net salary after tax."""
        return self.salary - self.calculate_tax()
    
    def __str__(self):
        return f"Gross: ${self.salary}, Tax: ${self.calculate_tax():.2f}, Net: ${self.calculate_net_salary():.2f}"

print("Task 5 - OOP Salary Calculator:")
calculator = EmployeeSalaryCalculator(50000)
print(calculator)  # Output: Gross: $50000, Tax: $10000.00, Net: $40000.00
print()

# ============================================================================
# TASK 6: Performance Optimization
# ============================================================================


def sum_even_numbers_legacy(limit):
    """Original inefficient approach."""
    total = 0
    for i in range(1, limit):
        if i % 2 == 0:
            total += i
    return total

def sum_even_numbers_optimized(limit):
    """Optimized using mathematical formula."""
    # Sum of even numbers: 2 + 4 + 6 + ... + n = n(n+2)/4
    n = (limit - 1) // 2
    return n * (n + 1)

print("Task 6 - Performance Optimization:")
limit = 1000000

start = time.time()
result_legacy = sum_even_numbers_legacy(limit)
legacy_time = time.time() - start

start = time.time()
result_optimized = sum_even_numbers_optimized(limit)
optimized_time = time.time() - start

print(f"Legacy result: {result_legacy}, Time: {legacy_time:.6f}s")
print(f"Optimized result: {result_optimized}, Time: {optimized_time:.6f}s")
print(f"Speedup: {legacy_time/optimized_time:.0f}x faster")
print()

# ============================================================================
# TASK 7: Removing Hidden Side Effects
# ============================================================================

def add_item(data, x):
    """Refactored: Return new data instead of mutating global state."""
    return data + [x]

print("Task 7 - Eliminating Side Effects:")
data = []
data = add_item(data, 10)
data = add_item(data, 20)
print(data)  # Output: [10, 20]
print()

# ============================================================================
# TASK 8: Refactoring Complex Input Validation
# ============================================================================

def is_password_valid(password):
    """Main validation function."""
    validators = [
        (lambda p: len(p) >= 8, "Password must be at least 8 characters"),
        (lambda p: any(c.isdigit() for c in p), "Must contain at least one digit"),
        (lambda p: any(c.isupper() for c in p), "Must contain at least one uppercase letter"),
    ]
    
    for validator, message in validators:
        if not validator(password):
            return False, message
    
    return True, "Valid Password"

print("Task 8 - Complex Validation Refactored:")
test_passwords = ["weak", "Password1", "PASSWORD1"]
for pwd in test_passwords:
    is_valid, message = is_password_valid(pwd)
    print(f"'{pwd}': {message}")
print()