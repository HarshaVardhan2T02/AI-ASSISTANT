"""Question 1: Zero-Shot Prompting (Leap Year Check)
Write a zero-shot prompt to generate a Python function that checks
whether a given year is a leap year.
Week2 -
Task:
• Record the AI-generated code.
• Test with years like 1900, 2000, 2024.
• Identify logical flaws or missing conditions."""

"""def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
# Testing
years = [1900, 2000, 2024]
for y in years:
    print(y, ":", is_leap_year(y))"""


"""Question 2: One-Shot Prompting (GCD of Two Numbers)
Write a one-shot prompt with one example to generate a Python
function that finds the Greatest Common Divisor (GCD) of two numbers.
Example:
Input: 12, 18 → Output: 6
Task:
• Compare with a zero-shot solution.
• Analyze algorithm efficiency."""

"""def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print(gcd(12, 18))"""


"""Question 3: Few-Shot Prompting (LCM Calculation)
Write a few-shot prompt with multiple examples to generate a Python
function that computes the Least Common Multiple (LCM).
Examples:
• Input: 4, 6 → Output: 12
• Input: 5, 10 → Output: 10
• Input: 7, 3 → Output: 21
Task:
• Examine how examples guide formula selection.
• Test edge cases."""
"""
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("LCM:", lcm(a, b))"""


"""Question 4: Zero-Shot Prompting (Binary to Decimal Conversion)
Write a zero-shot prompt to generate a Python function that converts a
binary number to decimal.
Task:
• Test with valid and invalid binary inputs.
• Identify missing validation logic."""
"""
def binary_to_decimal(binary):
    try:
        return int(binary, 2)
    except:
        return "Invalid Binary Number"
binary = input("Enter binary number: ")
print("Decimal:", binary_to_decimal(binary))
"""

"""
Question 5: One-Shot Prompting (Decimal to Binary Conversion)
Write a one-shot prompt with an example to generate a Python function
that converts a decimal number to binary.
Example:
Input: 10 → Output: 1010
Task:
• Compare clarity with zero-shot output.
• Analyze handling of zero and negative numbers."""


"""def decimal_to_binary(n):
    return bin(n).replace("0b", "")
num = int(input("Enter decimal number: "))
print("Binary:", decimal_to_binary(num))
"""

"""
Question 6: Few-Shot Prompting (Harshad Number Check)
Write a few-shot prompt to generate a Python function that checks
whether a number is a Harshad (Niven) number.
Examples:
• Input: 18 → Output: Harshad Number
• Input: 21 → Output: Harshad Number
• Input: 19 → Output: Not a Harshad Number
Task:
• Test boundary conditions.
• Evaluate robustness
"""

def is_harshad(n):
    digit_sum = sum(int(d) for d in str(n))
    if n % digit_sum == 0:
        return "Harshad Number"
    return "Not a Harshad Number"
num = int(input("Enter number: "))
print(is_harshad(num))
