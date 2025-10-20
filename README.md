# Simple Python Calculator with GitHub Actions CI/CD

A simple Python calculator application to demonstrate GitHub Actions CI/CD pipeline.

## Features

- Basic calculator operations (add, subtract, multiply, divide)
- Unit tests with pytest
- Automated CI/CD pipeline using GitHub Actions

## Project Structure

```
test_git_action/
├── calculator.py           # Main calculator module
├── test_calculator.py      # Unit tests
├── requirements.txt        # Python dependencies
├── .github/
│   └── workflows/
│       └── ci.yml         # GitHub Actions workflow
└── README.md              # This file
```

## Local Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python calculator.py
```

3. Run tests:
```bash
pytest test_calculator.py -v
```

## GitHub Setup

1. Initialize git repository:
```bash
git init
git add .
git commit -m "Initial commit: Simple calculator with CI/CD"
```

2. Create a new repository on GitHub (https://github.com/new)

3. Push to GitHub:
```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

## GitHub Actions CI/CD

The workflow (`.github/workflows/ci.yml`) will automatically:
- Run on every push to main/master branch
- Run on every pull request
- Test against Python versions 3.9, 3.10, and 3.11
- Install dependencies
- Run all unit tests
- Execute the calculator application

You can view the workflow runs in the "Actions" tab of your GitHub repository.

## License

This is a demo project for testing GitHub Actions.
