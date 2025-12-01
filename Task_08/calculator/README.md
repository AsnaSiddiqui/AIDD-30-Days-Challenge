# Simple Streamlit Calculator

This repository contains a simple web-based calculator application built using Streamlit.

## Features

-   Basic arithmetic operations: Addition (+), Subtraction (-), Multiplication (*), Division (/)
-   Supports integer and floating-point numbers.
-   Handles invalid input and division by zero with clear error messages.
-   Clean and user-friendly interface.

## Getting Started

Follow these instructions to set up and run the application locally.

### Prerequisites

-   Python 3.9+
-   `pip` (Python package installer)

### Setup and Run

1.  **Navigate to the project directory:**
    ```bash
    cd <your-project-directory>/calculator
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    ./venv/Scripts/activate
    # On macOS/Linux:
    # source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r calculator_app/requirements.txt
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run calculator_app/main.py
    ```

    This command will open the Streamlit application in your default web browser (usually at `http://localhost:8501`).

## Usage

1.  Enter an arithmetic expression (e.g., `10 + 5`, `25 * 3.5`, `100 / 4`) into the text input field.
2.  Click the "Calculate" button.
3.  The result will be displayed below the input field.
4.  If the expression is invalid or results in an error (e.g., division by zero), an appropriate error message will be shown.

## Project Structure

```
.
├── calculator_app/
│   ├── main.py        # Streamlit application entry point and UI
│   ├── calculator.py  # Core calculation logic and validation functions
│   └── requirements.txt # Project dependencies
├── tests/
│   └── unit/
│       └── test_calculator.py # Unit tests for calculation logic
├── specs/
│   └── 1-calculator-app/ # Feature specification and planning documents
│       ├── spec.md
│       ├── plan.md
│       ├── tasks.md
│       ├── research.md
│       │── data-model.md
│       ├── quickstart.md
│       └── checklists/
│           └── requirements.md
├── .gitignore         # Specifies intentionally untracked files to ignore
└── README.md          # This file
```
