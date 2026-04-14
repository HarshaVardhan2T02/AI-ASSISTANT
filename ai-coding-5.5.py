"""Task Description #1 (Transparency in Algorithm Optimization)
Task: Use AI to generate two solutions for checking prime
numbers:
• Naive approach(basic)
• Optimized approach
Prompt:
“Generate Python code for two prime-checking methods and
explain how the optimized version improves performance.”
Expected Output:
• Code for both methods.
• Transparent explanation of time complexity.
• Comparison highlighting efficiency improvements."""
"""import math

def is_prime_naive(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime_optimized(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

print("Naive Method:", "Prime Number" if is_prime_naive(num) else "Not Prime Number")
print("Optimized Method:", "Prime Number" if is_prime_optimized(num) else "Not Prime Number")

print("Naive Time Complexity: O(n)")
print("Optimized Time Complexity: O(√n)")"""



"""Task Description #2 (Transparency in Recursive Algorithms)
Objective: Use AI to generate a recursive function to calculate
Fibonacci numbers.
Instructions:
1. Ask AI to add clear comments explaining recursion.
2. Ask AI to explain base cases and recursive calls.
Expected Output:
• Well-commented recursive code.
• Clear explanation of how recursion works.
• Verification that explanation matches actual execution."""


"""def fibonacci(n):

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Enter Fibonacci index: "))
print(f"Fibonacci({n}) =", fibonacci(n)) """   


"""Task Description #3 (Transparency in Error Handling)
Task: Use AI to generate a Python program that reads a file and
processes data.
Prompt:
“Generate code with proper error handling and clear explanations
for each exception.”
Expected Output:
• Code with meaningful exception handling.
• Clear comments explaining each error scenario.
• Validation that explanations align with runtime behavior."""
"""try:
    file_name = input("Enter file name: ")
    with open(file_name, "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print("Error:", e)"""




    
    
    
"""Task Description #4 (Security in User Authentication)
Task: Use an AI tool to generate a Python-based login system.
Analyze: Check whether the AI uses secure password handling
practices.
Expected Output:
• Identification of security flaws (plain-text passwords, weak
validation).
• Revised version using password hashing and input validation.
• Short note on best practices for secure authentication."""

"""import hashlib

stored_username = "admin"
stored_password = hashlib.sha256("admin123".encode()).hexdigest()

username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

hashed_password = hashlib.sha256(password.encode()).hexdigest()

if username == stored_username and hashed_password == stored_password:
    print("Login Successful")
else:
    print("Invalid Login")"""


"""Task Description #5 (Privacy in Data Logging)
Task: Use an AI tool to generate a Python script that logs user
activity (username, IP address, timestamp).
Analyze: Examine whether sensitive data is logged unnecessarily
or insecurely.
Expected Output:
• Identified privacy risks in logging.
• Improved version with minimal, anonymized, or masked
logging.
• Explanation of privacy-aware logging principles.
"""

import datetime

username = input("Enter username: ")
ip_address = input("Enter IP address: ")

masked_username = username[0] + "***"
masked_ip = ip_address[:-3] + "***"

timestamp = datetime.datetime.now()

print("Log:", masked_username, masked_ip, timestamp)
