"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid base or argument for logarithm.")
    return math.log(b, a)


def exp(a, b):
    return a ** b


# Compatibility aliases if your partner's tests call these names:
logarithm = log


def square_root(x):
    if x < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(x)


def hypotenuse(a, b):
    return math.hypot(a, b)
