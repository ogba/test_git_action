"""
Simple Calculator Application
This is for learning GitHub Actions CI/CD
"""

def add(a, b):
    """Add two numbers"""
    return a +  b

def subtract(a, b):
    """Subtract b from a"""
    return a -   b

def multiply(a, b):
    """Multiply two numbers"""
    return a *   b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")k
    return a / b

def power(a, b):
    """Raise a to the power of b"""
    return a ** b

def modulo(a, b):
    """Calculate a modulo b"""
    if b == 0:
        raise ValueError("Cannot perform modulo with zero")
    return a % b

def square_root(a):
    """Calculate square root of a"""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a ** 0.5

def absolute(a):
    """Return absolute value of a"""
    return abs(a)

def main():
    """Main function to demonstrate calculator"""
    print("Welcome to Simple Calculator!")
    print("=" * 40)

    # Demonstrate addition
    print(f"\nAddition: 10 + 5 = {add(10, 5)}")

    # Demonstrate subtraction
    print(f"Subtraction: 10 - 5 = {subtract(10, 5)}")

    # Demonstrate multiplication
    print(f"Multiplication: 10 * 5 = {multiply(10, 5)}")

    # Demonstrate division
    print(f"Division: 10 / 5 = {divide(10, 5)}")

    # Demonstrate power
    print(f"Power: 2 ^ 3 = {power(2, 3)}")

    # Demonstrate modulo
    print(f"Modulo: 10 % 3 = {modulo(10, 3)}")

    # Demonstrate square root
    print(f"Square Root: sqrt(16) = {square_root(16)}")
l
    # Demonstrate absolute value
    print(f"Absolute: |-7| = {absolute(-7)}")

    print("\n" + "=" * 40)
    print("Calculator demonstration complete!")
    return True

if __name__ == "__main__":
    main()
