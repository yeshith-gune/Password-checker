# 🔐 Password Strength Checker

A Python tool that checks your password strength and whether it has appeared in known data breaches using the [HaveIBeenPwned API](https://haveibeenpwned.com/).

## 📋 Table of Contents
 
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Technologies Used](#-technologies-used)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Concepts Learned](#-concepts-learned)
- [Preview](#-preview)


---
 
## ✨ Features
 
- ✅ **Real-time strength analysis** — checks length, uppercase, lowercase, numbers and symbols
- ✅ **Breach database check** — verifies against 10 billion leaked passwords
- ✅ **k-Anonymity protection** — your actual password never leaves your device
- ✅ **Score system** — rates password from 0 to 5 with labels
- ✅ **Helpful suggestions** — tells you exactly what to improve
- ✅ **Hidden input** — password is invisible while typing
---

## 🔍 How It Works
 
### Strength Checker
The tool checks your password against **5 rules:**
 
| Rule | Requirement |
|---|---|
| ✅ Length | At least 8 characters |
| ✅ Uppercase | At least one capital letter (A–Z) |
| ✅ Lowercase | At least one small letter (a–z) |
| ✅ Number | At least one digit (0–9) |
| ✅ Symbol | At least one special character (!@#$...) |
 
Each rule passed adds **1 point** to the score (max = 5):
 
| Score | Label |
|---|---|
| 0 | Very Weak 🔴 |
| 1 | Weak 🔴 |
| 2 | Fair 🟠 |
| 3 | Moderate 🟡 |
| 4 | Strong 🟢 |
| 5 | Very Strong 💪 |
 

 


## Preview

![Password Checker Screenshot](assets/screenshot.PNG)
![Password Checker Screenshot](assets/screenshot1.PNG)

## 🔒 Security Note
 
This tool is built for **educational purposes** — to help you understand what makes a strong password. Never store or log real passwords anywhere. Always use a trusted password manager for your actual passwords.
 
---
<div align="center">
  <i>⭐ Star this repository if you found it helpful!</i>
</div>
