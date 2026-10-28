# Sequential Equation Parser
"""
Create a program that evaluates a mathematical expression from a string. The expression consists of non-negative integers separated by three possible operators: addition (+), subtraction (-), and multiplication ().
A key rule for this problem is that the expression must be evaluated strictly from left to right, ignoring the standard order of operations (like PEMDAS or BODMAS). For example, if the input is 3+52, the calculation should be (3+5)*2 which results in 16, not 3+(5*2) which would be 13.

Input:
A single line containing the expression as a string S. The string will only contain non-negative integers and the operators +, -, and *. It is guaranteed that the expression will always start and end with a number. Constraints: The length of the string S is between 1 and 50 characters, inclusive. The numbers in the expression are between 0 and 100, inclusive.

Output:
A single integer representing the final result of the left-to-right evaluation.
"""


def evaluate_expression(expr):
    # We can use a loop to parse the string into numbers and operators
    numbers = []
    operators = []
    
    current_num = ""
    
    for char in expr:
        if char.isdigit():
            current_num += char
        else:
            # If we hit an operator, save the number we just built
            numbers.append(int(current_num))
            current_num = "" # Reset for the next number
            operators.append(char)
            
    # Don't forget to append the very last number
    numbers.append(int(current_num))
    
    # Now we evaluate strictly left-to-right
    # Start with the first number
    result = numbers[0]
    
    # Loop through the operators and the remaining numbers
    for i in range(len(operators)):
        op = operators[i]
        next_num = numbers[i+1]
        
        if op == '+':
            result += next_num
        elif op == '-':
            result -= next_num
        elif op == '*':
            result *= next_num
            
    return result

expr = input("Enter expression: ")
final_result = evaluate_expression(expr)
print("Result:", final_result)