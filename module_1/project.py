import ast

def explain_arithmetic_expression(expression):
    """
    Explains a given arithmetic expression in a clear and informative way, handling unary minus correctly.

    Args:
        expression (str): The arithmetic expression to explain.

    Returns:
        str: A human-readable explanation of the expression.
    """

    try:
        # Use ast.literal_eval for safer expression evaluation
        result = ast.literal_eval(expression)
    except (SyntaxError, ValueError, ZeroDivisionError, NameError) as e:
        return f"Invalid expression: {e}"

    operators = ["+", "-", "*", "/", "//", "%", "**"]  # Include unary minus
    explanation = ""
    tokens = expression.split()

    for i, token in enumerate(tokens):
        if i == 0:
            explanation += f"Starting with the value {token}"
        elif token in operators:
            left_value = result
            operator = token
            right_value = tokens[i + 1]
            if token == "-" and i == 0:  # Handle unary minus
                explanation += f"\n  Taking the negative of {right_value}"
            else:
                explanation += f"\n  Performing {operator} with {right_value}"
        else:
            explanation += f" {token}"

        if i < len(tokens) - 1:
            # Use direct calculation for intermediate results
            result = eval(f"{left_value}{operator}{right_value}")  # Corrected line

    explanation += f"\n  = {result}\n"
    return explanation

# Example usage
expression = "10 + 2 * 3 - 1 // 2 ** 3"
explanation = explain_arithmetic_expression(expression)
print(explanation)

expression = "-10"  # Test unary minus
explanation = explain_arithmetic_expression(expression)
print(explanation)
