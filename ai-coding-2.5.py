"""Task 1: Refactoring Odd/Even Logic (List Version)
❖ Scenario:
You are improving legacy code.
❖ Task:
Write a program to calculate the sum of odd and even numbers in a list,
then refactor it using AI.
❖ Expected Output:
❖ Original and improved code

# Task 1: Odd/Even Sum with User Input
# Take list input from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# --- Original Logic ---
even_sum = 0
odd_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
print("\nOriginal Method")
print("Even Sum:", even_sum)
print("Odd Sum:", odd_sum)

# --- Improved Pythonic Logic ---
even_sum_new = sum(num for num in numbers if num % 2 == 0)
odd_sum_new = sum(num for num in numbers if num % 2 != 0)
print("\nImproved Method")
print("Even Sum:", even_sum_new)
print("Odd Sum:", odd_sum_new)"""



"""Task 2: Area Calculation Explanation
❖ Scenario:
You are onboarding a junior developer.
❖ Task:
Ask Gemini to explain a function that calculates the area of different
shapes.
❖ Expected Output:
➢ Code
➢ Explanation

# Task 2: Area Calculation with User Input
import math
def calculate_area(shape, value1, value2=0):
    if shape == "circle":
        return math.pi * value1 * value1
    elif shape == "rectangle":
        return value1 * value2
    elif shape == "triangle":
        return 0.5 * value1 * value2
    else:
        return "Invalid Shape"
shape = input("Enter shape (circle/rectangle/triangle): ").lower()
if shape == "circle":
    r = float(input("Enter radius: "))
    print("Area:", calculate_area(shape, r))
elif shape in ["rectangle", "triangle"]:
    v1 = float(input("Enter value1: "))
    v2 = float(input("Enter value2: "))
    print("Area:", calculate_area(shape, v1, v2))
else:
    print("Invalid Shape")"""


"""Task 3: Prompt Sensitivity Experiment
❖ Scenario:
You are testing how AI responds to different prompts.
❖ Task:
Use Cursor AI with different prompts for the same problem and observe
code changes.
❖ Expected Output:
➢ Prompt list
➢ Code variations

# Task 3: String Reversal Variations with User Input
text = input("Enter string: ")

# Simple Version
print("\nSimple Version:", text[::-1])

# Function Version
def reverse_string(s):
    return s[::-1]
print("Function Version:", reverse_string(text))

# Commented Version
def reverse_string_commented(text):
    # Reverse string using slicing
    return text[::-1]
print("Commented Version:", reverse_string_commented(text))"""


"""Task 4: Tool Comparison Reflection
❖ Scenario:
You must recommend an AI coding tool.
❖ Task:
Based on your work in this topic, compare Gemini, Copilot, and Cursor AI
for usability and code quality.
❖ Expected Output:
Short written reflection"""

# Task 4: AI Tool Comparison with User Input

tools = {
    "copilot": {
        "Name": "GitHub Copilot",
        "Usability": "Very Easy (IDE Integrated)",
        "Code Quality": "High"
    },
    "gemini": {
        "Name": "Gemini",
        "Usability": "Easy (Chat Based)",
        "Code Quality": "Good"
    },
    "cursor": {
        "Name": "Cursor AI",
        "Usability": "Moderate",
        "Code Quality": "Good"
    }
}

choice = input("Enter tool (copilot/gemini/cursor): ").lower()

if choice in tools:
    print("\nTool Details:")
    for key, value in tools[choice].items():
        print(f"{key}: {value}")
else:
    print("Invalid Tool Choice")
