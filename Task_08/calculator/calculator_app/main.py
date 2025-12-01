"""
This is the main Streamlit application for the Simple Streamlit Calculator.
It provides a web interface for users to enter arithmetic expressions and view results or error messages.
"""
import streamlit as st
from calculator import validate_expression, calculate_expression

# Set the title of the Streamlit application
st.title("Simple Streamlit Calculator")

# Create a text input field for the user to enter their arithmetic expression
expression_input = st.text_input("Enter arithmetic expression:", "")

# Create a button to trigger the calculation
calculate_button = st.button("Calculate")

# Logic to execute when the 'Calculate' button is pressed
if calculate_button:
    if not expression_input.strip(): # Check for empty or whitespace-only input
        st.error("Please enter an expression.")
    elif not validate_expression(expression_input):
        # If validation fails (due to disallowed characters, syntax errors, etc.)
        st.error("Invalid input or syntax. Please check your expression.")
    else:
        # If the expression passes initial validation, attempt to calculate
        try:
            result = calculate_expression(expression_input)
            # Display the result using st.metric for a prominent display
            st.metric(label="Result", value=result)
        except ZeroDivisionError:
            # Catch specific division by zero error
            st.error("Error: Division by zero is not allowed.")
        except ValueError as e:
            # Catch general value errors (e.g., unsupported operations)
            st.error(f"Error: {e}")
        except Exception as e:
            # Catch any other unexpected errors
            st.error(f"An unexpected error occurred: {e}")
