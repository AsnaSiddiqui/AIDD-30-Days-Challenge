"""
This module provides functions for validating and calculating arithmetic expressions.
It includes safety checks to prevent code injection and handles common arithmetic errors.
"""
import ast
import operator

# Define allowed operators and characters for expression validation
ALLOWED_OPERATORS = ['+', '-', '*', '/']
ALLOWED_CHARACTERS = "0123456789.+-*/ " # Includes digits, decimal, operators, and space

def validate_expression(expression: str) -> bool:
    """
    Validates if the expression contains only allowed characters and is syntactically valid.

    Args:
        expression (str): The arithmetic expression string to validate.

    Returns:
        bool: True if the expression is valid, False otherwise.
    """
    # Check for empty or whitespace-only expression
    if not expression.strip():
        return False

    # Check if all characters in the expression are allowed
    for char in expression:
        if char not in ALLOWED_CHARACTERS:
            return False

    # Attempt to parse the expression to check for syntax errors.
    # ast.parse with mode='eval' expects a single expression, not arbitrary code.
    try:
        ast.parse(expression, mode='eval')
    except (SyntaxError, ValueError): # Catch common parsing errors
        return False
    
    return True

def calculate_expression(expression: str) -> float | int:
    """
    Safely evaluates an arithmetic expression.
    Handles basic operations: +, -, *, /
    Prevents execution of arbitrary code by using Python's AST (Abstract Syntax Tree).

    Args:
        expression (str): The arithmetic expression string to evaluate.

    Returns:
        float | int: The result of the evaluation.

    Raises:
        ZeroDivisionError: If the expression involves division by zero.
        ValueError: If the expression is invalid or contains unsupported operations.
    """
    # Helper function to recursively evaluate AST nodes
    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        elif isinstance(node, ast.BinOp): # Binary operations (e.g., a + b)
            left = _eval(node.left)
            right = _eval(node.right)
            if isinstance(node.op, ast.Add):
                return operator.add(left, right)
            elif isinstance(node.op, ast.Sub):
                return operator.sub(left, right)
            elif isinstance(node.op, ast.Mult):
                return operator.mul(left, right)
            elif isinstance(node.op, ast.Div):
                if right == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                return operator.truediv(left, right) # True division for floats
            else:
                raise TypeError("Unsupported binary operator type.")
        elif isinstance(node, ast.UnaryOp): # Unary operations (e.g., -a)
            operand = _eval(node.operand)
            if isinstance(node.op, ast.UAdd): # Unary plus
                return operand
            elif isinstance(node.op, ast.USub): # Unary minus
                return operator.neg(operand)
            else:
                raise TypeError("Unsupported unary operator type.")
        # Handle number literals. ast.Num is for Python < 3.9, ast.Constant for >= 3.9
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.Constant):
            # Ensure the constant is a number type
            if isinstance(node.value, (int, float)):
                return node.value
            else:
                raise TypeError(f"Unsupported constant type: {type(node.value).__name__}")
        else:
            raise TypeError(f"Unsupported AST node type: {node.__class__.__name__}")

    try:
        # Parse the expression into an Abstract Syntax Tree
        # mode='eval' ensures that only expressions (not arbitrary statements) are parsed.
        return _eval(ast.parse(expression, mode='eval'))
    except (SyntaxError, TypeError, ValueError, ZeroDivisionError) as e:
        # Re-raise parsing/evaluation errors as a ValueError for consistency
        raise ValueError(f"Invalid expression or operation: {e}")