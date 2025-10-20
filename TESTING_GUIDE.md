# Testing Guide for Calculator CI/CD

## Overview
This project demonstrates a complete CI/CD pipeline using GitHub Actions with comprehensive testing for a simple calculator application.

## Project Structure
```
.
├── main.py                    # Calculator with 8 operations
├── test_main.py              # Comprehensive test suite (47 tests)
├── requirements.txt          # Python dependencies (pytest)
├── .github/
│   └── workflows/
│       └── python-app.yml    # GitHub Actions CI/CD workflow
├── .gitignore               # Git ignore file
└── TESTING_GUIDE.md         # This file
```

## Calculator Operations

The calculator supports 8 operations:
1. **Addition** - Add two numbers
2. **Subtraction** - Subtract two numbers
3. **Multiplication** - Multiply two numbers
4. **Division** - Divide two numbers (with zero check)
5. **Power** - Raise number to a power
6. **Modulo** - Get remainder of division (with zero check)
7. **Square Root** - Calculate square root (with negative check)
8. **Absolute** - Get absolute value

## What Gets Tested

### 1. Addition Tests (5 tests)
- Positive numbers
- Negative numbers
- Mixed numbers
- Zero values
- Decimal numbers

### 2. Subtraction Tests (5 tests)
- Positive numbers
- Negative numbers
- Mixed numbers
- Zero values
- Decimal numbers

### 3. Multiplication Tests (6 tests)
- Positive numbers
- Negative numbers
- Mixed numbers
- Multiplication by zero
- Multiplication by one
- Decimal numbers

### 4. Division Tests (6 tests)
- Positive numbers
- Negative numbers
- Mixed numbers
- Division by zero (error handling)
- Zero divided by number
- Decimal numbers

### 5. Power Tests (5 tests)
- Positive exponent
- Zero exponent
- Negative exponent
- Negative base
- Decimal exponent

### 6. Modulo Tests (5 tests)
- Positive numbers
- Even division
- Negative numbers
- Modulo by zero (error handling)
- Smaller by larger

### 7. Square Root Tests (6 tests)
- Perfect squares
- Non-perfect squares
- Zero
- One
- Negative numbers (error handling)
- Decimal numbers

### 8. Absolute Value Tests (4 tests)
- Positive numbers
- Negative numbers
- Zero
- Decimal numbers

### 9. Main Function Tests (2 tests)
- Returns True on success
- Executes without errors

### 10. Integration Tests (3 tests)
- Combined operations
- Order of operations
- All operations return numbers

**Total: 47 tests**

## Running Tests Locally

### Run all tests with verbose output:
```bash
pytest test_main.py -v
```

### Run tests in quiet mode:
```bash
pytest test_main.py -q
```

### Run tests with coverage report:
```bash
pip install pytest-cov
pytest test_main.py --cov=main --cov-report=term-missing
```

### Run specific test class:
```bash
pytest test_main.py::TestAddition -v
pytest test_main.py::TestDivision -v
```

### Run specific test:
```bash
pytest test_main.py::TestDivision::test_divide_by_zero_raises_error -v
```

### Run the calculator demo:
```bash
python main.py
```

## GitHub Actions Workflow

The workflow runs automatically on:
- Every push to the `main` branch
- Every pull request to the `main` branch

### Workflow Steps:
1. **Checkout code** - Gets the latest code from repository
2. **Set up Python 3.11** - Installs Python environment
3. **Display Python version** - Shows which Python version is being used
4. **Install dependencies** - Installs pytest from requirements.txt
5. **Run calculator demo** - Executes main.py to verify it works
6. **Run calculator tests** - Runs all 47 tests with pytest
7. **Generate coverage report** - Shows code coverage percentage
8. **Success message** - Confirms all tests passed

## How to Trigger the CI/CD Pipeline

1. Make changes to your code
2. Commit and push to GitHub:
```bash
git add .
git commit -m "Your commit message"
git push origin main
```

3. View the workflow:
   - Go to your GitHub repository
   - Click "Actions" tab
   - See your workflow running in real-time
   - Check test results and logs

## What Happens if Tests Fail?

If any test fails:
- GitHub Actions workflow will FAIL ❌
- You'll see which test failed in the Actions log
- The workflow will stop and not proceed
- You'll get a notification (if enabled)
- The commit will be marked with a red X

## Success Indicators

When everything passes:
- All 47 tests show PASSED ✅
- Coverage report is generated
- Success message displays
- Commit gets a green checkmark ✓
- Ready for deployment/merge

## Example Output

```
============================= test session starts =============================
test_main.py::TestAddition::test_add_positive_numbers PASSED     [  2%]
test_main.py::TestAddition::test_add_negative_numbers PASSED     [  4%]
...
test_main.py::TestIntegration::test_all_operations_return_numbers PASSED [100%]

============================== 47 passed in 0.06s ==============================
```

## Error Handling Tests

The calculator includes proper error handling:
- **Division by zero** - Raises ValueError
- **Modulo by zero** - Raises ValueError
- **Square root of negative** - Raises ValueError

These are all tested to ensure errors are caught properly!

## Tips for Learning

1. **Make a small change** - Try modifying a calculator function
2. **Watch tests fail** - Push the change and see which tests catch it
3. **Fix the issue** - Update the code to make tests pass
4. **See green pipeline** - Watch GitHub Actions show success

## Example Learning Exercise

Try this:
1. Remove the zero check in the `divide()` function
2. Run tests locally: `pytest test_main.py -v`
3. See `test_divide_by_zero_raises_error` fail
4. Restore the zero check
5. See all tests pass again

This is a complete CI/CD learning environment with real error handling!
