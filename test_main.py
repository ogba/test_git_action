"""
Test suite for main.py calculator functions
This will be run by GitHub Actions on every push/pull request
"""

import pytest
from main import add, subtract, multiply, divide, power, modulo, square_root, absolute, main


class TestAddition:
    """Test cases for addition operation"""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers"""
        assert add(5, 3) == 8
        assert add(10, 20) == 30

    def test_add_negative_numbers(self):
        """Test adding two negative numbers"""
        assert add(-5, -3) == -8
        assert add(-10, -20) == -30

    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers"""
        assert add(5, -3) == 2
        assert add(-10, 20) == 10

    def test_add_with_zero(self):
        """Test adding with zero"""
        assert add(0, 5) == 5
        assert add(10, 0) == 10
        assert add(0, 0) == 0

    def test_add_decimal_numbers(self):
        """Test adding decimal numbers"""
        assert add(1.5, 2.5) == 4.0
        assert add(0.1, 0.2) == pytest.approx(0.3)


class TestSubtraction:
    """Test cases for subtraction operation"""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(10, 5) == 5
        assert subtract(20, 8) == 12

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers"""
        assert subtract(-5, -3) == -2
        assert subtract(-10, -20) == 10

    def test_subtract_mixed_numbers(self):
        """Test subtracting mixed positive and negative"""
        assert subtract(5, -3) == 8
        assert subtract(-10, 5) == -15

    def test_subtract_with_zero(self):
        """Test subtracting with zero"""
        assert subtract(10, 0) == 10
        assert subtract(0, 5) == -5

    def test_subtract_decimal_numbers(self):
        """Test subtracting decimal numbers"""
        assert subtract(5.5, 2.5) == 3.0
        assert subtract(1.0, 0.1) == pytest.approx(0.9)


class TestMultiplication:
    """Test cases for multiplication operation"""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers"""
        assert multiply(5, 3) == 15
        assert multiply(10, 4) == 40

    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers"""
        assert multiply(-5, -3) == 15
        assert multiply(-2, -10) == 20

    def test_multiply_mixed_numbers(self):
        """Test multiplying mixed numbers"""
        assert multiply(5, -3) == -15
        assert multiply(-4, 10) == -40

    def test_multiply_by_zero(self):
        """Test multiplying by zero"""
        assert multiply(5, 0) == 0
        assert multiply(0, 10) == 0
        assert multiply(0, 0) == 0

    def test_multiply_by_one(self):
        """Test multiplying by one"""
        assert multiply(5, 1) == 5
        assert multiply(1, 10) == 10

    def test_multiply_decimal_numbers(self):
        """Test multiplying decimal numbers"""
        assert multiply(2.5, 4) == 10.0
        assert multiply(1.5, 2.0) == 3.0


class TestDivision:
    """Test cases for division operation"""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers"""
        assert divide(10, 2) == 5.0
        assert divide(20, 4) == 5.0

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers"""
        assert divide(-10, -2) == 5.0
        assert divide(-20, -4) == 5.0

    def test_divide_mixed_numbers(self):
        """Test dividing mixed numbers"""
        assert divide(10, -2) == -5.0
        assert divide(-20, 4) == -5.0

    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises ValueError"""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_divide_zero_by_number(self):
        """Test dividing zero by a number"""
        assert divide(0, 5) == 0.0

    def test_divide_decimal_numbers(self):
        """Test dividing decimal numbers"""
        assert divide(10.0, 2.5) == 4.0
        assert divide(7.5, 3) == 2.5


class TestPower:
    """Test cases for power operation"""

    def test_power_positive_exponent(self):
        """Test raising to positive exponent"""
        assert power(2, 3) == 8
        assert power(5, 2) == 25

    def test_power_zero_exponent(self):
        """Test raising to zero power"""
        assert power(5, 0) == 1
        assert power(100, 0) == 1

    def test_power_negative_exponent(self):
        """Test raising to negative exponent"""
        assert power(2, -1) == 0.5
        assert power(4, -2) == 0.0625

    def test_power_with_negative_base(self):
        """Test power with negative base"""
        assert power(-2, 3) == -8
        assert power(-2, 2) == 4

    def test_power_decimal_exponent(self):
        """Test power with decimal exponent"""
        assert power(4, 0.5) == 2.0
        assert power(27, 1/3) == pytest.approx(3.0)


class TestModulo:
    """Test cases for modulo operation"""

    def test_modulo_positive_numbers(self):
        """Test modulo with positive numbers"""
        assert modulo(10, 3) == 1
        assert modulo(20, 6) == 2

    def test_modulo_even_division(self):
        """Test modulo when division is even"""
        assert modulo(10, 5) == 0
        assert modulo(20, 4) == 0

    def test_modulo_negative_numbers(self):
        """Test modulo with negative numbers"""
        assert modulo(-10, 3) == 2
        assert modulo(10, -3) == -2

    def test_modulo_by_zero_raises_error(self):
        """Test that modulo by zero raises ValueError"""
        with pytest.raises(ValueError, match="Cannot perform modulo with zero"):
            modulo(10, 0)

    def test_modulo_smaller_by_larger(self):
        """Test modulo when dividend is smaller"""
        assert modulo(3, 10) == 3
        assert modulo(5, 20) == 5


class TestSquareRoot:
    """Test cases for square root operation"""

    def test_square_root_perfect_squares(self):
        """Test square root of perfect squares"""
        assert square_root(4) == 2.0
        assert square_root(9) == 3.0
        assert square_root(16) == 4.0

    def test_square_root_non_perfect_squares(self):
        """Test square root of non-perfect squares"""
        assert square_root(2) == pytest.approx(1.414, rel=1e-2)
        assert square_root(5) == pytest.approx(2.236, rel=1e-2)

    def test_square_root_of_zero(self):
        """Test square root of zero"""
        assert square_root(0) == 0.0

    def test_square_root_of_one(self):
        """Test square root of one"""
        assert square_root(1) == 1.0

    def test_square_root_negative_raises_error(self):
        """Test that square root of negative raises ValueError"""
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            square_root(-4)

    def test_square_root_decimal(self):
        """Test square root of decimal numbers"""
        assert square_root(6.25) == 2.5
        assert square_root(0.25) == 0.5


class TestAbsolute:
    """Test cases for absolute value operation"""

    def test_absolute_positive_number(self):
        """Test absolute value of positive number"""
        assert absolute(5) == 5
        assert absolute(100) == 100

    def test_absolute_negative_number(self):
        """Test absolute value of negative number"""
        assert absolute(-5) == 5
        assert absolute(-100) == 100

    def test_absolute_zero(self):
        """Test absolute value of zero"""
        assert absolute(0) == 0

    def test_absolute_decimal(self):
        """Test absolute value of decimal numbers"""
        assert absolute(-3.5) == 3.5
        assert absolute(7.8) == 7.8


class TestMain:
    """Test cases for main function"""

    def test_main_returns_true(self):
        """Test that main function returns True on success"""
        result = main()
        assert result == True

    def test_main_executes_without_error(self):
        """Test that main function executes without raising exceptions"""
        try:
            main()
            assert True
        except Exception as e:
            pytest.fail(f"main() raised exception: {e}")


class TestIntegration:
    """Integration tests for calculator operations"""

    def test_combined_operations(self):
        """Test combining multiple operations"""
        result = add(multiply(2, 3), divide(10, 2))
        assert result == 11.0

    def test_order_of_operations(self):
        """Test proper order of operations"""
        result = subtract(power(2, 3), modulo(10, 3))
        assert result == 7

    def test_all_operations_return_numbers(self):
        """Test that all operations return numeric values"""
        assert isinstance(add(1, 2), (int, float))
        assert isinstance(subtract(5, 3), (int, float))
        assert isinstance(multiply(2, 3), (int, float))
        assert isinstance(divide(10, 2), (int, float))
        assert isinstance(power(2, 3), (int, float))
        assert isinstance(modulo(10, 3), (int, float))
        assert isinstance(square_root(4), (int, float))
        assert isinstance(absolute(-5), (int, float))


if __name__ == "__main__":
    # Run tests with verbose output
    pytest.main([__file__, "-v", "--tb=short"])
