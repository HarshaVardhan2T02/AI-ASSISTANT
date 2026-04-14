"""
Lab Experiment: Documentation Generation - Automatic documentation and code comments
This module demonstrates various documentation styles and their applications.
"""

# ============================================================================
# PROBLEM 1: String Utilities Function
# ============================================================================

def reverse_string(text):
    """
    Reverse a given string.
    
    Args:
        text (str): The string to reverse.
    
    Returns:
        str: The reversed string.
    
    Example:
        >>> reverse_string("hello")
        'olleh'
    """
    # Use Python's slice notation with step -1 to reverse
    return text[::-1]


# ============================================================================
# PROBLEM 2: Password Strength Checker
# ============================================================================

def check_strength(password):
    """
    Check if password meets minimum strength requirements.
    
    Args:
        password (str): The password to validate.
    
    Returns:
        bool: True if password length >= 8 characters, False otherwise.
    
    Note:
        This is a basic check. For production, implement robust validation
        including uppercase, lowercase, digits, and special characters.
    """
    # Minimum password length requirement is 8 characters
    return len(password) >= 8


# ============================================================================
# PROBLEM 3: Math Utilities Module
# ============================================================================

def square(n):
    """
    Calculate the square of a number.
    
    Args:
        n (int/float): The number to square.
    
    Returns:
        int/float: The square of the input number.
    """
    return n * n


def cube(n):
    """
    Calculate the cube of a number.
    
    Args:
        n (int/float): The number to cube.
    
    Returns:
        int/float: The cube of the input number.
    """
    return n * n * n


def factorial(n):
    """
    Calculate factorial of a non-negative integer.
    
    Args:
        n (int): A non-negative integer.
    
    Returns:
        int: The factorial of n.
    
    Raises:
        ValueError: If n is negative.
    """
    # Validate input
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive calculation
    return n * factorial(n - 1)


# ============================================================================
# PROBLEM 4: Attendance Management Module
# ============================================================================

class AttendanceManager:
    """
    Manage student attendance records.
    
    Attributes:
        attendance (dict): Dictionary storing attendance status for students.
    """
    
    def __init__(self):
        """Initialize the attendance manager with an empty record."""
        self.attendance = {}
    
    def mark_present(self, student):
        """
        Mark a student as present.
        
        Args:
            student (str): The name of the student.
        """
        self.attendance[student] = "Present"
    
    def mark_absent(self, student):
        """
        Mark a student as absent.
        
        Args:
            student (str): The name of the student.
        """
        self.attendance[student] = "Absent"
    
    def get_attendance(self, student):
        """
        Get attendance status of a student.
        
        Args:
            student (str): The name of the student.
        
        Returns:
            str: Attendance status or "Not recorded" if not found.
        """
        return self.attendance.get(student, "Not recorded")


# ============================================================================
# PROBLEM 5: File Handling Function
# ============================================================================

def read_file(filename):
    """
    Read and return the entire contents of a file.
    
    Args:
        filename (str): Path to the file to read.
    
    Returns:
        str: The complete file contents.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If an error occurs while reading the file.
    
    Example:
        >>> content = read_file("example.txt")
    """
    # Open file in read mode and read all contents
    with open(filename, 'r') as f:
        return f.read()


# ============================================================================
# DOCUMENTATION STYLES COMPARISON
# ============================================================================
"""
COMPARISON OF DOCUMENTATION STYLES:

1. DOCSTRING STYLE (PEP 257):
   - Standard Python convention
   - Triple-quoted strings
   - Best for: General-purpose libraries
   - Advantage: Extracted by help() function

2. INLINE COMMENTS:
   - Code clarification with # symbols
   - Best for: Complex logic explanation
   - Advantage: Contextual explanation of "why"

3. GOOGLE-STYLE DOCUMENTATION:
   - Structured format with Args, Returns, Raises sections
   - Best for: Large projects and team collaboration
   - Advantage: Tools can auto-generate documentation (Sphinx, pdoc)

RECOMMENDATIONS:
- String Utilities: Google-style (for library reusability)
- Password Checker: Google-style + Inline comments (security-critical)
- Math Utils: Docstring (simple functions)
- Attendance Module: Google-style (class-based, scalable)
- File Handling: Google-style (handles exceptions explicitly)
"""