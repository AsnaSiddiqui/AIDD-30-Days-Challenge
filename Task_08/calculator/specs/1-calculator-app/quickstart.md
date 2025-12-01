# Quickstart: Calculator Web Application

**Date**: 2025-12-01

This document outlines the basic steps to set up and run the Calculator Web Application locally.

## Prerequisites

-   Python 3.9+ installed
-   `pip` (Python package installer)

## Setup and Run

1.  **Clone the repository (if not already done):**
    ```bash
    git clone [REPOSITORY_URL]
    cd calculator
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ./venv/Scripts/activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r calculator_app/requirements.txt
    ```
    (Note: `calculator_app/requirements.txt` will be created during implementation.)
4.  **Run the Streamlit application:**
    ```bash
    streamlit run calculator_app/main.py
    ```
    (Note: `calculator_app/main.py` will be created during implementation.)

This will open the Streamlit application in your web browser.
