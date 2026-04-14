"""
Lab 13: Code Refactoring – Improving Legacy Code with AI Suggestions
Complete Solution for All Tasks
"""

# ============================================================================
# TASK 1: Refactoring – Removing Code Duplication (Rectangle Calculations)
# ============================================================================

class Rectangle: 
    """
    A class to represent a rectangle and calculate its properties.
    
    Attributes:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    """
    
    def __init__(self, length, width):
        """Initialize rectangle with length and width."""
        self.length = length
        self.width = width
    
    def area(self):
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: The area (length * width)
        """
        return self.length * self.width
    
    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        
        Returns:
            float: The perimeter (2 * (length + width))
        """
        return 2 * (self.length + self.width)
    
    def display(self):
        """Display rectangle area and perimeter."""
        print(f"Area of Rectangle: {self.area()}")
        print(f"Perimeter of Rectangle: {self.perimeter()}")


def task_1_demo():
    """Demonstrate Task 1 refactoring."""
    print("\n=== TASK 1: Rectangle Refactoring ===")
    rectangles = [
        Rectangle(5, 10),
        Rectangle(7, 12),
        Rectangle(10, 15)
    ]
    for rect in rectangles:
        rect.display()


# ============================================================================
# TASK 2: Refactoring – Extracting Reusable Functions (Price Calculation)
# ============================================================================

def calculate_total(price, tax_rate=0.18):
    """
    Calculate total price including tax.
    
    Args:
        price (float): The base price
        tax_rate (float): Tax rate as decimal (default: 0.18)
    
    Returns:
        float: Total price after tax
    """
          
    tax = price * tax_rate
    return price + tax


def task_2_demo():
    """Demonstrate Task 2 refactoring."""
    print("\n=== TASK 2: Price Calculation Refactoring ===")
    prices = [250, 500]
    for price in prices:
        total = calculate_total(price)
        print(f"Total Price: {total}")


# ============================================================================
# TASK 3: Refactoring Using Classes (Grade Calculator)
# ============================================================================

class GradeCalculator:
    """
    A class to calculate grades based on student marks.
    
    This class encapsulates the logic for determining letter grades
    from numerical marks following standard grading criteria.
    """
    
    def calculate_grade(self, marks):
        """
        Calculate the grade based on marks.
        
        Args:
            marks (int/float): Student's marks (0-100)
        
        Returns:
            str: The corresponding grade (Grade A, B, C, D, or Fail)
        """
        if marks >= 90:
            return "Grade A"
        elif marks >= 80:
            return "Grade B"
        elif marks >= 70:
            return "Grade C"
        elif marks >= 40:
            return "Grade D"
        else:
            return "Fail"


def task_3_demo():
    """Demonstrate Task 3 refactoring."""
    print("\n=== TASK 3: Grade Calculator Refactoring ===")
    calculator = GradeCalculator()
    student_marks = [85, 72, 95, 38, 65]
    for marks in student_marks:
        grade = calculator.calculate_grade(marks)
        print(f"Marks: {marks} → {grade}")


# ============================================================================
# TASK 4: Refactoring – Converting Procedural Code to Functions (Square)
# ============================================================================

def get_input(prompt="Enter number: "):
    """
    Get integer input from user.
    
    Args:
        prompt (str): The input prompt
    
    Returns:
        int: The integer input by user
    """
    return int(input(prompt))


def calculate_square(num):
    """
    Calculate the square of a number.
    
    Args:
        num (int/float): The number to square
    
    Returns:
        int/float: The square of the number
    """
    return num * num


def display_result(label, value):
    """
    Display a result with label.
    
    Args:
        label (str): Description of the result
        value: The value to display
    """
    print(f"{label}: {value}")


def task_4_demo():
    """Demonstrate Task 4 refactoring."""
    print("\n=== TASK 4: Procedural to Functional Refactoring ===")
    num = 5  # Using hardcoded value for demo
    square = calculate_square(num)
    display_result("Square", square)


# ============================================================================
# TASK 5: Refactoring Procedural Code into OOP (Employee Salary)
# ============================================================================

class EmployeeSalaryCalculator:
    """
    A class to calculate employee salary and deductions.
    
    Attributes:
        salary (float): The gross salary of the employee
        tax_rate (float): Tax rate as decimal (default: 0.2)
    """
    
    def __init__(self, salary, tax_rate=0.2):
        """
        Initialize salary calculator.
        
        Args:
            salary (float): The gross salary
            tax_rate (float): Tax rate (default: 0.2 or 20%)
        """
        self.salary = salary
        self.tax_rate = tax_rate
    
    def calculate_tax(self):
        """
        Calculate tax amount.
        
        Returns:
            float: Tax amount
        """
        return self.salary * self.tax_rate
    
    def calculate_net_salary(self):
        """
        Calculate net salary after tax deduction.
        
        Returns:
            float: Net salary
        """
        return self.salary - self.calculate_tax()
    
    def display_salary_breakdown(self):
        """Display detailed salary breakdown."""
        print(f"Gross Salary: {self.salary}")
        print(f"Tax (20%): {self.calculate_tax()}")
        print(f"Net Salary: {self.calculate_net_salary()}")


def task_5_demo():
    """Demonstrate Task 5 refactoring."""
    print("\n=== TASK 5: OOP Salary Calculator ===")
    calculator = EmployeeSalaryCalculator(50000)
    calculator.display_salary_breakdown()


# ============================================================================
# TASK 6: Optimizing Search Logic (Using Sets)
# ============================================================================

class AccessControl:
    """
    A class to manage user access control using efficient data structures.
    
    Uses sets for O(1) lookup time instead of O(n) linear search.
    """
    
    def __init__(self, users=None):
        """
        Initialize access control with authorized users.
        
        Args:
            users (list): List of authorized usernames
        """
        self.authorized_users = set(users) if users else set()
    
    def check_access(self, username):
        """
        Check if user has access.
        
        Args:
            username (str): The username to verify
        
        Returns:
            bool: True if user is authorized, False otherwise
        """
        return username in self.authorized_users


def task_6_demo():
    """Demonstrate Task 6 refactoring."""
    print("\n=== TASK 6: Optimized Search Using Sets ===")
    access = AccessControl(["admin", "guest", "editor", "viewer"])
    test_users = ["admin", "hacker"]
    for user in test_users:
        result = "Access Granted" if access.check_access(user) else "Access Denied"
        print(f"{user}: {result}")


# ============================================================================
# TASK 8: Fibonacci Generator
# ============================================================================

def generate_fibonacci(n):
    """
    Generate Fibonacci sequence up to n terms.
    
    Args:
        n (int): Number of Fibonacci numbers to generate
    
    Returns:
        list: List containing first n Fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence


def task_8_demo():
    """Demonstrate Task 8 refactoring."""
    print("\n=== TASK 8: Fibonacci Generator ===")
    n = 10
    fib_series = generate_fibonacci(n)
    print(f"Fibonacci series up to {n} terms: {fib_series}")


# ============================================================================
# TASK 9: Twin Primes Checker
# ============================================================================

def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): The number to check
    
    Returns:
        bool: True if prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_twin_prime(p1, p2):
    """
    Check if two numbers are twin primes.
    
    Twin primes are pairs of prime numbers that differ by 2.
    
    Args:
        p1 (int): First number
        p2 (int): Second number
    
    Returns:
        bool: True if both are prime and differ by 2, False otherwise
    """
    return is_prime(p1) and is_prime(p2) and abs(p1 - p2) == 2


def task_9_demo():
    """Demonstrate Task 9 refactoring."""
    print("\n=== TASK 9: Twin Primes Checker ===")
    test_pairs = [(11, 13), (17, 19), (5, 7), (10, 12)]
    for p1, p2 in test_pairs:
        result = "Twin Primes" if is_twin_prime(p1, p2) else "Not Twin Primes"
        print(f"({p1}, {p2}): {result}")


# ============================================================================
# TASK 10: Chinese Zodiac Program
# ============================================================================

def get_zodiac(year):
    """
    Get the Chinese Zodiac sign for a given year.
    
    Args:
        year (int): The year to look up
    
    Returns:
        str: The corresponding Chinese Zodiac sign
    """
    zodiac_signs = [
        "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox",
        "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat"
    ]
    return zodiac_signs[year % 12]


def task_10_demo():
    """Demonstrate Task 10 refactoring."""
    print("\n=== TASK 10: Chinese Zodiac ===")
    test_years = [2000, 2021, 2024]
    for year in test_years:
        zodiac = get_zodiac(year)
        print(f"{year}: {zodiac}")


# ============================================================================
# TASK 11: Harshad (Niven) Number Checker
# ============================================================================

def is_harshad(number):
    """
    Check if a number is a Harshad (Niven) number.
    
    A Harshad number is divisible by the sum of its digits.
    
    Args:
        number (int): The number to check
    
    Returns:
        bool: True if Harshad number, False otherwise
    """
    if number <= 0:
        return False
    
    digit_sum = sum(int(digit) for digit in str(number))
    return number % digit_sum == 0


def task_11_demo():
    """Demonstrate Task 11 refactoring."""
    print("\n=== TASK 11: Harshad Number Checker ===")
    test_numbers = [18, 19, 21, 12]
    for num in test_numbers:
        result = "Yes" if is_harshad(num) else "No"
        print(f"{num}: {result}")


# ============================================================================
# TASK 12: Factorial Trailing Zeros
# ============================================================================

def count_trailing_zeros(n):
    """
    Count trailing zeros in n! (factorial of n).
    
    Optimized approach: Count multiples of 5 in n!
    (since there are always more factors of 2 than 5)
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        int: Number of trailing zeros in n!
    """
    if n < 0:
        return 0
    
    count = 0
    power_of_5 = 5
    while power_of_5 <= n:
        count += n // power_of_5
        power_of_5 *= 5
    return count


def task_12_demo():
    """Demonstrate Task 12 refactoring."""
    print("\n=== TASK 12: Factorial Trailing Zeros ===")
    test_numbers = [5, 10, 25, 100]
    for n in test_numbers:
        zeros = count_trailing_zeros(n)
        print(f"{n}! has {zeros} trailing zeros")


# ============================================================================
# TASK 13: Collatz Sequence Generator
# ============================================================================

def generate_collatz_sequence(n):
    """
    Generate the Collatz sequence starting from n.
    
    Rules:
    - If n is even: next = n / 2
    - If n is odd: next = 3n + 1
    - Continue until reaching 1
    
    Args:
        n (int): Starting number (must be positive)
    
    Returns:
        list: The complete Collatz sequence
    """
    if n <= 0:
        return []
    
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def task_13_demo():
    """Demonstrate Task 13 refactoring."""
    print("\n=== TASK 13: Collatz Sequence Generator ===")
    test_numbers = [6, 1, 27]
    for num in test_numbers:
        seq = generate_collatz_sequence(num)
        print(f"Collatz({num}): {seq}")


# ============================================================================
# TASK 14: Lucas Number Sequence
# ============================================================================

def generate_lucas_sequence(n):
    """
    Generate Lucas sequence up to n terms.
    
    Lucas sequence starts with 2, 1 and follows: Ln = Ln-1 + Ln-2
    
    Args:
        n (int): Number of terms to generate
    
    Returns:
        list: First n Lucas numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [2]
    
    lucas = [2, 1]
    for i in range(2, n):
        lucas.append(lucas[i-1] + lucas[i-2])
    return lucas


def task_14_demo():
    """Demonstrate Task 14 refactoring."""
    print("\n=== TASK 14: Lucas Number Sequence ===")
    for n in [1, 5, 10]:
        seq = generate_lucas_sequence(n)
        print(f"Lucas({n}): {seq}")


# ============================================================================
# TASK 15: Vowel & Consonant Counter
# ============================================================================

def count_vowels_consonants(text):
    """
    Count vowels and consonants in a string.
    
    Args:
        text (str): Input string to analyze
    
    Returns:
        tuple: (vowel_count, consonant_count)
    """
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count


def task_15_demo():
    """Demonstrate Task 15 refactoring."""
    print("\n=== TASK 15: Vowel & Consonant Counter ===")
    test_strings = ["hello", "aeiou", ""]
    for text in test_strings:
        vowels, consonants = count_vowels_consonants(text)
        print(f"'{text}': Vowels={vowels}, Consonants={consonants}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("LAB 13: CODE REFACTORING - COMPLETE SOLUTION")
    print("=" * 70)
    
    task_1_demo()
    task_2_demo()
    task_3_demo()
    task_4_demo()
    task_5_demo()
    task_6_demo()
    task_8_demo()
    task_9_demo()
    task_10_demo()
    task_11_demo()
    task_12_demo()
    task_13_demo()
    task_14_demo()
    task_15_demo()
    
    print("\n" + "=" * 70)
    print("All tasks completed successfully!")
    print("=" * 70)