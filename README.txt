# CyberSafe Toolkit 🛡️

A simple Python-based cybersecurity toolkit that helps users analyze password strength and identify potentially suspicious URLs. This project is designed for beginners learning cybersecurity concepts and Python programming.

## 🚀 Features

### 1. Password Strength Analyzer

Evaluates a password based on common security best practices:

* Minimum length of 8 characters
* Presence of uppercase letters
* Presence of lowercase letters
* Presence of numbers
* Presence of special characters

**Password Ratings:**

* Weak Password
* Medium Password
* Strong Password

### 2. URL Security Checker

Performs basic checks to identify potentially suspicious URLs by looking for:

* Use of `http://` instead of secure `https://`
* Presence of `@` symbols
* Hyphens (`-`) in the URL
* Common phishing-related keywords such as:

  * login
  * verify
  * secure
  * update
  * bank
  * account

**URL Ratings:**

* Potentially Suspicious URL
* URL Appears Safer

## 📋 Requirements

* Python 3.x

No external libraries are required. The project uses Python's built-in `re` module.

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/sandrasaneesh/CyberSafeToolkit.git
```

Navigate to the project directory:

```bash
cd CyberSafeToolkit
```

## ▶️ Usage

Run the script:

```bash
python cybersafe_toolkit.py
```

You will see:

```text
===== CyberSafe Toolkit =====
1. Password Strength Analyzer
2. URL Security Checker
3. Exit
```

Choose an option and follow the prompts.

### Example 1: Password Analysis

```text
Choose an option: 1
Enter a password: MyPassword123!

Password Analysis Result:
Strong Password
```

### Example 2: URL Analysis

```text
Choose an option: 2
Enter URL: http://secure-bank-login.com

URL Analysis Result:
Potentially Suspicious URL
```

## 📂 Project Structure

```text
CyberSafeToolkit/
│
├── cybersafe_toolkit.py
└── README.md
```

## 🎯 Learning Objectives

This project demonstrates:

* Python conditional statements
* User input handling
* Regular expressions (`re`)
* Basic cybersecurity concepts
* Password security assessment
* Phishing URL detection techniques

## ⚠️ Disclaimer

This tool provides basic educational analysis and should not be considered a complete cybersecurity solution. Real-world password auditing and phishing detection require more advanced techniques and security tools.

## 🤝 Contributing

Contributions, improvements, and suggestions are welcome. Feel free to fork the repository and submit a pull request.

## 📜 License

This project is open source and available under the MIT License.

---

Developed with Python for learning cybersecurity fundamentals.
