#import pytest
# from calculator import Calculator
# def test_add():
#     calc = Calculator()
#     assert calc.add(3, 5) == 8
#     assert calc.add(-1, 1) == 0
#     assert calc.add(-1, -1) == -2
# def test_subtract():
#     calc = Calculator()
#     assert calc.subtract(5, 3) == 2
#     assert calc.subtract(1, 5) == -4
#     assert calc.subtract(-5, -3) == -2

# def test_multiply():
#     calc = Calculator()
#     assert calc.multiply(3.23, 4) == 12            
#     assert calc.multiply(-2, 5) == -10          
#     assert calc.multiply(0, 100) == 0 

# def test_divide():
#     calc = Calculator()
#     assert calc.divide(9, 3) == 3.0
#     assert calc.divide(4.5, 1.5) == 3.0
#     assert calc.divide(5, 0)
# import pytest
# from calculator import Calculator

# @pytest.mark.parametrize("a, b, expected", [
#     (3, 5, 8),
#     (-1, 1, 0),
#     (-1, -1, -2),
#     (0, 0, 0),
#     (2.5, 3.5, 6.0)
# ])
# def test_add_parameterized(a, b, expected):
#     """Test addition with various number combinations"""
#     calc = Calculator()
#     assert calc.add(a, b) == expected

# @pytest.mark.parametrize("a, b, expected", [
#     (5, 3, 2),
#     (1, 5, -4),
#     (-5, -3, -2),
#     (0, 5, -5),
#     (5.5, 2.5, 3.0)
# ])
# def test_subtract_parameterized(a, b, expected):
#     """Test subtraction with edge cases"""
#     calc = Calculator()
#     assert calc.subtract(a, b) == expected

# @pytest.mark.parametrize("a, b, expected", [
#     (3, 4, 12),
#     (-2, 5, -10),
#     (0, 100, 0),
#     (2.5, 4.0, 10.0),
#     (-1.5, -2.0, 3.0)
# ])
# def test_multiply_parameterized(a, b, expected):
#     """Test multiplication with different number types"""
#     calc = Calculator()
#     assert calc.multiply(a, b) == expected


# @pytest.mark.parametrize("a, b, expected", [
#     (10, 2, 5.0),      # Normal division
#     (5, 2, 2.5),       # Decimal division
#     (9, 3, 3.0),       # Integer result
#     (4.5, 1.5, 3.0),   # Floating-point division
#     (0, 5, 0.0),       # Zero dividend
#     (5, 0, "Cannot divide by zero")  # Division by zero (returns string)
# ])
# def test_divide(a, b, expected):
#     calc = Calculator()
#     assert calc.divide(a, b) == expected

# @pytest.mark.parametrize("base, exponent, expected", [
#     # Positive exponents
#     (2, 3, 8),          # 2^3 = 8
#     (5, 2, 25),         # 5^2 = 25
#     (3, 0, 1),          # Any number^0 = 1
# ])

# def test_power(base, exponent, expected):
#     calc = Calculator()
#     assert calc.power(base, exponent) == pytest.approx(expected)

import pytest
from calculator import Calculator

@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),        # Positive numbers
    (-1, 1, 0),       # Negative + Positive
    (-1, -1, -2),     # Negative numbers
    (0, 0, 0),        # Zeros
    (2.5, 3.5, 6.0)   # Floats
])
def test_add_parameterized(calculator, a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (1, 5, -4),
    (-5, -3, -2),
    (5.5, 2.5, 3.0)
])
def test_subtract_parameterized(calculator, a, b, expected):
    assert calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (-2, 5, -10),
    (2.5, 4.0, 10.0)
])
def test_multiply_parameterized(calculator, a, b, expected):
    assert calculator.multiply(a, b) == pytest.approx(expected)

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (5, 2, 2.5),
    (4.5, 1.5, 3.0),
    (4.5, 1.5, 3.0),
])
def test_divide_parameterized(calculator, a, b, expected):
    assert calculator.divide(a, b) == pytest.approx(expected)

def test_divide_by_zero(calculator):
    """Test division by zero raises ValueError"""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(5, 0)

@pytest.mark.parametrize("a, b, expected", [
(2, 3, 8),
(3, 2, 9),
(2, 0, 1),
(2, -2, 0.25), # Should be 1/(2^2) = 0.25
])

def test_power_parameterized(calculator, a, b, expected):
    assert calculator.power(a, b) == pytest.approx(expected)

@pytest.mark.parametrize("n, expected", [
    (5, 120),         # 5! = 120
    (7, 5040),        
    (10, 3628800),    
    (0, 1),          
    (1, 1),           
])
def test_factorial(calculator, n, expected):
    assert calculator.factorial(n) == expected

@pytest.mark.parametrize("n, expected", [
    (5, 5),          
    (10, 55),         
    (15, 610),        
    (0, 0),           
    (1, 1),           
    (2, 1),          
])
def test_fibonacci(calculator, n, expected):
    assert calculator.fibonacci(n) == expected


def test_addition_rounding(precise_calculator):
    assert precise_calculator.add(1.234, 2.345) == round(1.234 + 2.345, precise_calculator.precision)