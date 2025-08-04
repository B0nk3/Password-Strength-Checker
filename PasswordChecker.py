import re
import string
password = input("Enter the password:")
strength = int(0)
warning = False
if len(password) > 8:
    strength += 1
else:
    print("Password too short")
    warning = True
if len(password) > 12:
    strength += 1

if any(char in string.punctuation for char in password):
    strength += 1
else:
    print("Add special characters")
    warning = True
if re.search(r"[a-z]", password):
    strength += 1
if re.search(r"[A-Z]", password):
    strength += 1
if re.search(r"[0-9]", password):
    strength += 1
else:
    warning = True
    print("Password need to contain numbers")

CommonPassowrds = ["password", "123456", "qwerty", "admin"]
if password.lower() in (p.lower() for p in CommonPassowrds):
    warning = True
    print("Password is too common")

if re.search(r"(.)\1{2,}", password):
    print("Password should not use repetitions of the same character")    
    warning = True
if not warning:

    if strength < 3:
     print("Weak")
    elif strength >= 3 and strength < 5:
        print("Medium")
    else:
        print("Strong")