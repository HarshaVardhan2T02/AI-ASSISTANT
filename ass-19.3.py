import pandas as pd

# Lab 19 - Code Translation: Converting Between Programming Languages
# File: ass-19.3.py

# ============================================================================
# TASK 1: Python to C++ Conversion
# ============================================================================
# Original Python Class: Student

class Student:
    """Python Student class with attributes and methods"""
    def __init__(self, name, student_id, gpa):
        self.name = name
        self.student_id = student_id
        self.gpa = gpa
    
    def display_info(self):
        return f"Name: {self.name}, ID: {self.student_id}, GPA: {self.gpa}"
    
    def update_gpa(self, new_gpa):
        self.gpa = new_gpa
        return f"GPA updated to {self.gpa}"


# Testing Task 1
print("=" * 60)
print("TASK 1: Python to C++ Conversion")
print("=" * 60)
student1 = Student("Alice", 101, 3.8)
print(student1.display_info())
print(student1.update_gpa(3.9))
print()


# ============================================================================
# TASK 2: Java to Python Function Conversion
# ============================================================================
# Converting Java isPrime() method to Python

def is_prime(number):
    """
    Check whether a number is prime.
    Java equivalent converted to Python.
    """
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


# Testing Task 2
print("=" * 60)
print("TASK 2: Java to Python Function Conversion (isPrime)")
print("=" * 60)
test_numbers = [2, 3, 4, 17, 20, 29, 50, 97]
for num in test_numbers:
    print(f"{num} is prime: {is_prime(num)}")
print()


# ============================================================================
# TASK 3: Pseudocode to Python Implementation
# ============================================================================
# Pseudocode: Bubble Sort Algorithm

def bubble_sort(arr):
    """
    Bubble Sort Algorithm - Translated from Pseudocode
    Pseudocode:
        for i = 0 to length(arr) - 1
            for j = 0 to length(arr) - i - 1
                if arr[j] > arr[j+1]
                    swap arr[j] and arr[j+1]
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def selection_sort(arr):
    """
    Selection Sort Algorithm - Translated from Pseudocode
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Testing Task 3
print("=" * 60)
print("TASK 3: Pseudocode to Python Implementation (Sorting)")
print("=" * 60)
sample_list1 = [64, 34, 25, 12, 22, 11, 90]
sample_list2 = [64, 34, 25, 12, 22, 11, 90]

print(f"Original list: {sample_list1}")
print(f"Bubble Sort: {bubble_sort(sample_list1.copy())}")
print(f"Selection Sort: {selection_sort(sample_list2.copy())}")
print()


# ============================================================================
# TASK 4: SQL to Pandas Query
# ============================================================================
# SQL Query: SELECT name, salary FROM employees WHERE salary > 50000


# Create sample DataFrame
employees_data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'salary': [55000, 48000, 65000, 52000, 72000, 45000],
    'department': ['IT', 'HR', 'IT', 'Finance', 'IT', 'HR']
}

df_employees = pd.DataFrame(employees_data)

# SQL equivalent: SELECT name, salary FROM employees WHERE salary > 50000
result_df = df_employees[df_employees['salary'] > 50000][['name', 'salary']]


# Testing Task 4
print("=" * 60)
print("TASK 4: SQL to Pandas Query")
print("=" * 60)
print("Original DataFrame:")
print(df_employees)
print("\nSQL Query: SELECT name, salary FROM employees WHERE salary > 50000")
print("Pandas Equivalent: df_employees[df_employees['salary'] > 50000][['name', 'salary']]")
print("\nResult:")
print(result_df)
print()


# ============================================================================
# TASK 5: Real-Time Application - Algorithm Translation
# ============================================================================
# Python: Linear Search Algorithm

def linear_search(arr, target):
    """
    Linear Search in Python
    Time Complexity: O(n)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    """
    Binary Search in Python (requires sorted array)
    Time Complexity: O(log n)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Testing Task 5
print("=" * 60)
print("TASK 5: Real-Time Application - Algorithm Translation")
print("=" * 60)
search_arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target_val = 50

print(f"Array: {search_arr}")
print(f"Target: {target_val}")
print(f"Linear Search Result (Index): {linear_search(search_arr, target_val)}")
print(f"Binary Search Result (Index): {binary_search(search_arr, target_val)}")
print(f"\nSearching for non-existent value (100):")
print(f"Linear Search Result: {linear_search(search_arr, 100)}")
print(f"Binary Search Result: {binary_search(search_arr, 100)}")
print()

print("=" * 60)
print("ALL TASKS COMPLETED SUCCESSFULLY")
print("=" * 60)