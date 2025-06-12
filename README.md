# 🔐 Password Complexity Checker

This is a simple Python script that checks whether a password meets standard security requirements. It evaluates password strength based on common cybersecurity guidelines and uses colored terminal output to clearly indicate which criteria are met or missing.

## 📋 Features

- ✅ Checks if password is at least 12 characters long  
- ✅ Verifies the presence of:
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit
  - At least one special character (e.g. `!@#$%^&*`)
- ✅ Uses colored output to make results easy to read (green = passed, red = failed)

## 💻 Requirements

- Python 3.x
- `termcolor` library

Install `termcolor` using pip:

```bash
pip install termcolor
