# Problem Statement 1: AI-Assisted Bug Detection
# Bug: range(1, n) should be range(1, n+1) to include n in the multiplication

def factorial(n):
	"""
	Calculate the factorial of n.
	
	Args:
		n (int): A non-negative integer
		
	Returns:
		int: The factorial of n
		
	Example:
		>>> factorial(5)
		120
	"""
	if n < 0:
		raise ValueError("Factorial is not defined for negative numbers")
	if n == 0 or n == 1:
		return 1
	result = 1
	for i in range(1, n + 1):  # Fixed: was range(1, n), now range(1, n+1)
		result = result * i
	return result


# Problem Statement 2: Improving Readability & Documentation

def perform_arithmetic_operation(operand1, operand2, operation):
	"""
	Perform arithmetic operations on two operands.
	
	Args:
		operand1 (float): The first number
		operand2 (float): The second number
		operation (str): The operation to perform ('add', 'sub', 'mul', 'div')
		
	Returns:
		float: The result of the operation
		
	Raises:
		ValueError: If operation is not recognized or division by zero occurs
		TypeError: If operands are not numeric
		
	Example:
		>>> perform_arithmetic_operation(10, 5, 'add')
		15
		>>> perform_arithmetic_operation(10, 5, 'div')
		2.0
	"""
	if not isinstance(operand1, (int, float)) or not isinstance(operand2, (int, float)):
		raise TypeError("Operands must be numeric")
	
	if operation == "add":
		return operand1 + operand2
	elif operation == "sub":
		return operand1 - operand2
	elif operation == "mul":
		return operand1 * operand2
	elif operation == "div":
		if operand2 == 0:
			raise ValueError("Division by zero is not allowed")
		return operand1 / operand2
	else:
		raise ValueError(f"Unknown operation: {operation}")


# Problem Statement 3: Enforcing Coding Standards

def check_prime(n):
	"""
	Check if a number is prime.
	
	Args:
		n (int): The number to check
		
	Returns:
		bool: True if n is prime, False otherwise
	"""
	if n < 2:
		return False
	for i in range(2, int(n ** 0.5) + 1):  # Optimized: check up to sqrt(n)
		if n % i == 0:
			return False
	return True


# Problem Statement 4: AI as a Code Reviewer in Real Projects

from typing import List, Union

def double_even_numbers(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
	"""
	Double all even numbers in a list.
	
	Args:
		numbers (List[Union[int, float]]): A list of numeric values
		
	Returns:
		List[Union[int, float]]: A list of doubled even numbers
		
	Raises:
		TypeError: If input is not a list or contains non-numeric elements
		
	Example:
		>>> double_even_numbers([1, 2, 3, 4, 5])
		[4, 8]
	"""
	if not isinstance(numbers, list):
		raise TypeError("Input must be a list")
	
	result = []
	for num in numbers:
		if not isinstance(num, (int, float)):
			raise TypeError(f"All elements must be numeric, got {type(num)}")
		if num % 2 == 0:
			result.append(num * 2)
	return result


# Problem Statement 5: AI-Assisted Performance Optimization

def sum_of_squares(numbers):
	"""
	Calculate the sum of squares of numbers (optimized version).
	
	Args:
		numbers (List[int]): A list of numbers
		
	Returns:
		int: The sum of squares
		
	Example:
		>>> sum_of_squares([1, 2, 3, 4, 5])
		55
	"""
	return sum(x * x for x in numbers)  # Optimized: uses generator expression


# Test all functions
if __name__ == "__main__":
	print("Problem 1 - Factorial:")
	print(f"factorial(5) = {factorial(5)}")  # Expected: 120
	
	print("\nProblem 2 - Arithmetic Operations:")
	print(f"add(10, 5) = {perform_arithmetic_operation(10, 5, 'add')}")  # 15
	print(f"div(10, 5) = {perform_arithmetic_operation(10, 5, 'div')}")  # 2.0
	
	print("\nProblem 3 - Check Prime:")
	print(f"check_prime(17) = {check_prime(17)}")  # True
	print(f"check_prime(10) = {check_prime(10)}")  # False
	
	print("\nProblem 4 - Double Even Numbers:")
	print(f"double_even_numbers([1, 2, 3, 4, 5]) = {double_even_numbers([1, 2, 3, 4, 5])}")  # [4, 8]
	
	print("\nProblem 5 - Sum of Squares:")
	print(f"sum_of_squares([1, 2, 3, 4, 5]) = {sum_of_squares([1, 2, 3, 4, 5])}")  # 55
