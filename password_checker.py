import re
import hashlib
import getpass
import requests


# ── STRENGTH CHECKER ──────────────────────────────────────────────────────────

def check_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("** Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("** Add at least one uppercase letter (A-Z).")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("** Add at least one lowercase letter (a-z).")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("** Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("** Add at least one special character (!@#$%...).")

    labels = {0: "Very Weak ", 1: "Weak ", 2: "Fair ",
              3: "Moderate ", 4: "Strong ", 5: "Very Strong "}

    return score, labels[score], feedback


# ── HAVEIBEENPWNED API ─────────────────────────────────────────────────────────

def check_pwned(password):
    sha1_hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    try:
        response = requests.get(
            f"https://api.pwnedpasswords.com/range/{prefix}",
            timeout=5
        )
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"**  API error: {e}")
        return -1

    for line in response.text.splitlines():
        returned_suffix, count = line.split(":")
        if returned_suffix == suffix:
            return int(count)

    return 0


# ── MAIN ───────────────────────────────────────────────────────────────────────

def main():
    print("=" * 45)
    print("       ** Password Strength Checker")
    print("=" * 45)

    password = getpass.getpass("Enter your password (hidden): ")

    if not password:
        print("No password entered. Exiting.")
        return

    print("\n** Analyzing your password...\n")

    score, label, feedback = check_strength(password)
    print(f"Strength: {label}  ({score}/5)")

    if feedback:
        print("\nSuggestions to improve:")
        for tip in feedback:
            print(f"  {tip}")
    else:
        print("** Your password meets all strength requirements!")

    print("\n** Checking HaveIBeenPwned database...")
    times_found = check_pwned(password)

    if times_found == -1:
        print("**  Breach check skipped (API unreachable).")
    elif times_found == 0:
        print("** This password has NOT been found in any known data breach.")
    else:
        print(f"** WARNING: Found {times_found:,} times in data breaches!")
        print("   Do NOT use this password.")

    print("\n" + "=" * 45)


if __name__ == "__main__":
    main()
