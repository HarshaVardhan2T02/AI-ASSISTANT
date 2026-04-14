"""AI-Generated Logic Without Modularization (String Reversal Without
Functions)
❖ Scenario
You are developing a basic text-processing utility for a messaging
application.
❖ Task Description
Use GitHub Copilot to generate a Python program that:
➢ Reverses a given string
➢ Accepts user input
➢ Implements the logic directly in the main code
➢ Does not use any user-defined functions
❖ Expected Output
➢ Correct reversed string
➢ Screenshots showing Copilot-generated code suggestions
➢ Sample inputs and outputs




Efficiency & Logic Optimization (Readability Improvement)
❖ Scenario
The code will be reviewed by other developers.
❖ Task Description
Examine the Copilot-generated code from Task 1 and improve it by:
➢ Removing unnecessary variables
➢ Simplifying loop or indexing logic
➢ Improving readability
➢ Use Copilot prompts like:
▪ “Simplify this string reversal code”
▪ “Improve readability and efficiency”
Hint:
Prompt Copilot with phrases like
“optimize this code”, “simplify logic”, or “make it more readable”
❖ Expected Output
➢ Original and optimized code versions
➢ Explanation of how the improvements reduce time complexity

# Original Loop Based Reversal

user_string = input("Enter a string: ")

reversed_string = ""
for char in user_string:
    reversed_string = char + reversed_string

print("Reversed String:", reversed_string)

Task 3: Modular Design Using AI Assistance (String Reversal Using Functions)
❖ Scenario
The string reversal logic is needed in multiple parts of an application.
❖ Task Description
Use GitHub Copilot to generate a function-based Python program that:
➢ Uses a user-defined function to reverse a string
➢ Returns the reversed string
➢ Includes meaningful comments (AI-assisted)
❖ Expected Output
➢ Correct function-based implementation
➢ Screenshots documenting Copilot’s function generation
➢ Sample test cases and outputs"""

def reverse_string(s):
    """Reverses the input string s and returns the reversed version.
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
# Testing the function
input_string = "Hello, World!"
print("Original String:", input_string)
print("Reversed String:", reverse_string(input_string))
# Explanation of the function
# The reverse_string function takes a string s as input and initializes an empty string reversed_str.
# It iterates through each character in the input string s, prepending it to reversed_str
# This effectively builds the reversed string as it processes each character.
# Finally, the function returns the fully reversed string.

Task 4: Comparative Analysis – Procedural vs Modular Approach (With vs
Without Functions)
❖ Scenario
You are asked to justify design choices during a code review.
❖ Task Description
Compare the Copilot-generated programs:
➢ Without functions (Task 1)
➢ With functions (Task 3)
Analyze them based on:
➢ Code clarity
➢ Reusability
➢ Debugging ease
➢ Suitability for large-scale applications
❖ Expected Output
Comparison table or short analytical report

# Comparison Analysis
# | Aspect              | Without Functions                     | With Functions                        |
# |---------------------|---------------------------------------|---------------------------------------|
# | Code Clarity        | Less clear due to inline logic        | More clear with separation
# | Reusability         | Low, logic is not reusable            | High, function can be reused          |
# | Debugging Ease      | Harder to debug due to intertwined logic | Easier to
# | Suitability for Large-Scale Apps | Not suitable, hard to maintain        | Suitable, promotes modular design     |

# Without Function
string1 = "Hello"
rev1 = string1[::-1]
print(rev1)
string2 = "World"
rev2 = string2[::-1]
print(rev2)

# With Function 
def reverse_string(s):
    return s[::-1]
print(reverse_string("Hello"))
print(reverse_string("World"))
# Explanation
# The version without functions is less clear because the logic for reversing the string is directly embedded in the main code, making it harder to read and understand at a glance. It also lacks reusability, as the reversal logic cannot be easily reused for different strings without copying and pasting code.
# In contrast, the version with functions is more clear and organized. The reversal logic is encapsulated within a function, making it easier to read and understand. It promotes reusability, as the function can be called with different strings without needing to duplicate code. This modular approach is more suitable for large-scale applications, as it allows for better maintenance and scalability. 

Task 5: AI-Generated Iterative vs Recursive Fibonacci Approaches (Different
Algorithmic Approaches to String Reversal)
❖ Scenario
Your mentor wants to evaluate how AI handles alternative logic paths.
❖ Task Description
Prompt GitHub Copilot to generate:
➢ A loop-based string reversal approach
➢ A built-in / slicing-based string reversal approach
❖ Expected Output
➢ Two correct implementations
➢ Comparison discussing:
▪ Execution flow
▪ Time complexity
▪ Performance for large inputs
▪ When each approach is appropriate"""

# Loop-Based Approach   
def reverse_string_loop(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
# Built-in / Slicing-Based Approach
def reverse_string_slice(s):
    return s[::-1]
# Testing the functions
input_string = "Hello, World!"
print("Loop-Based Reversal:", reverse_string_loop(input_string))
print("Slicing-Based Reversal:", reverse_string_slice(input_string))
# Explanation
# The loop-based approach iteratively builds the reversed string by prepending each character, resulting in a time complexity of O(n^2) due to string concatenation. The slicing-based approach uses Python's slicing syntax, which is optimized and runs in O(n) time complexity. For large inputs, the slicing approach is more efficient and should be preferred. The loop-based approach may be more suitable for educational purposes to illustrate the concept of string reversal, while the slicing approach is better for practical use in production code. 
