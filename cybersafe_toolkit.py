import re

print("===== CyberSafe Toolkit =====")
print("1. Password Strength Analyzer")
print("2. URL Security Checker")
print("3. Exit")

choice = input("Choose an option: ")

if choice == "1":

    password = input("Enter a password: ")

    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"\d", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    print("\nPassword Analysis Result:")

    if score <= 2:
        print("Weak Password")
    elif score <= 4:
        print("Medium Password")
    else:
        print("Strong Password")

elif choice == "2":

    url = input("Enter URL: ")

    suspicious_keywords = [
        "login",
        "verify",
        "secure",
        "update",
        "bank",
        "account"
    ]

    score = 0

    if "http://" in url:
        score += 1

    if "@" in url:
        score += 1

    if "-" in url:
        score += 1

    for word in suspicious_keywords:
        if word in url.lower():
            score += 1

    print("\nURL Analysis Result:")

    if score >= 3:
        print("Potentially Suspicious URL")
    else:
        print("URL Appears Safer")

elif choice == "3":
    print("Goodbye!")

else:
    print("Invalid Option")