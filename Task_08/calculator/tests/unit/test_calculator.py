import pytest
from calculator_app.calculator import validate_expression, calculate_expression # Assuming validate_expression exists and is imported

def test_validate_expression_valid():
    assert validate_expression("1+1") is True
    assert validate_expression("1.0 - 0.5") is True
    assert validate_expression("10 * 2") is True
    assert validate_expression("100 / 50") is True
    assert validate_expression(" 1 + 2 ") is True # With spaces
    assert validate_expression("1234567890.0987654321 + 1") is True

def test_calculate_expression_basic():
    assert calculate_expression("1+1") == 2
    assert calculate_expression("1.0 - 0.5") == 0.5
    assert calculate_expression("10 * 2") == 20
    assert calculate_expression("100 / 50") == 2.0
    assert calculate_expression(" 5 + 5 ") == 10
    assert calculate_expression("10 / 3") == pytest.approx(3.3333333333333335)
    assert calculate_expression("2 * 3 + 1") == 7 # Test order of operations
    assert calculate_expression("1 + 2 * 3") == 7 # Test order of operations