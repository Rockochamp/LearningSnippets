import requests
import hashlib
import re

def is_common_password(password):
    # Hash the password using SHA-1
    password_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    
    # Get the first 5 characters of the hash (prefix) and the remaining characters (suffix)
    prefix, suffix = password_hash[:5], password_hash[5:]
    
    # Check if the suffix is in the "Have I Been Pwned" database
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code == 200:
        hash_suffixes = [line.split(":")[0] for line in response.text.splitlines()]
        return suffix in hash_suffixes

    return False

def is_password_strong(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False
    
    # Check if the password contains both uppercase and lowercase letters
    if not any(char.islower() and char.isupper() for char in password):
        return False
    
    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Check if the password contains at least one special character
    special_characters = "!@#$%^&*()_+[]{}|;:,.<>?-="
    if not any(char in special_characters for char in password):
        return False
    
    # Check if the password is a common password
    if is_common_password(password):
        return False
    
    # Check if the password contains common patterns (e.g., "12345")
    if re.search(r'(\d{5,})', password):
        return False
    
    return True

def password_strength_meter(password):
    strength = 0
    
    # Check the length of the password
    if len(password) >= 8:
        strength += 1

    # Check if the password contains uppercase and lowercase letters
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        strength += 1

    # Check if the password contains at least one digit
    if any(char.isdigit() for char in password):
        strength += 1

    # Check if the password contains special characters
    if any(char in "!@#$%^&*()_+[]{}|;:,.<>?-=" for char in password):
        strength += 1

    return strength

# Get the user's password input
password = input("Enter your password: ")

# Check the password strength
strength = password_strength_meter(password)

if strength == 4:
    print("Your password is very strong. Excellent choice!")
elif strength == 3:
    print("Your password is strong. Good job!")
elif strength == 2:
    print("Your password is moderate. Consider adding more complexity.")
elif strength == 1:
    print("Your password is weak. Please follow password recommendations.")
else:
    print("Your password is too short. Please choose a longer password.")

# Check if the password is common or contains known patterns
if is_common_password(password):
    print("Warning: Your password is a common password and can be easily guessed.")
