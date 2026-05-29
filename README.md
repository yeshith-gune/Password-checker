# ** Password Strength Checker

A Python tool that checks your password strength and whether it has appeared in known data breaches using the [HaveIBeenPwned API](https://haveibeenpwned.com/).

## Features
- Checks password strength (length, uppercase, lowercase, numbers, symbols)
- Verifies if the password was leaked in a breach (without sending the password online)
- Uses k-Anonymity for safe API calls

## How to Run

Install the required library:
```bash
pip install requests
```

Run the script:
```bash
python password_checker.py
```

## How It Works
Your password is hashed locally using SHA-1. Only the first 5 characters of the hash are sent to the API — your actual password never leaves your computer.

## Preview

![Password Checker Screenshot](assets/screenshot.PNG)
![Password Checker Screenshot](assets/screenshot1.PNG)

## Here upgraded version of password-checker
see in here 
https://passgurd.vercel.app/
