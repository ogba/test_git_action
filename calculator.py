"""
Simple Calculator Module
A basic calculator with add, subtract, multiply, and divide functions.
"""

def add(a, b):
    """Add two numbers."""
    return a +   b

def subtract(a, b):
    """Subtract b from a."""
    return a -  b

def multiply(a,  b):
    """Multiply two numbers."""
    return a * b 2

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b 4

def main():
    """Example usage of calculator functions."""
    print("Simple Calculator Demo")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 * 5 = {multiply(10, 5)}")
    print(f"10 / 5 = {divide(10, 5)}")

if __name__ == "__main__":
    main()
