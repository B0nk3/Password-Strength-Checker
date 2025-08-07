import re
import string
import hashlib
import requests
import tkinter as tk
from tkinter import messagebox

def check_pwned_password(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5 = sha1_password[:5]
    tail = sha1_password[5:]
    url = f"https://api.pwnedpasswords.com/range/{first5}"
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}")

    hashes = (line.split(':') for line in res.text.splitlines())
    for h,count in hashes:
        if h == tail:
            return int(count)
    return 0




        
def check_password():
    password = entry.get()
    strength = 0
    warnings = []
    if len(password) > 8:
        strength += 1
    else:
        warnings.append("Password too short")
    if len(password) > 12:
        strength += 1

    if any(char in string.punctuation for char in password):
        strength += 1
    else:
        warnings.append("Add special characters")
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        warnings.append("Password need to contain numbers")

    if warnings:
        messagebox.showwarning('weak password', '\n'. join(warnings))
    else:
        if strength < 3:
             print("Weak")
        elif strength >= 3 and strength < 5:
            print("Medium")
        else:
            print("Strong")
    if re.search(r"(.)\1{2,}", password):
        print("Password should not use repetitions of the same character")    
        warning = True
    if not warnings:
        pwned_count = check_pwned_password(password)
        if(pwned_count > 0):
            print(f"Password has been found {pwned_count} times in data breaches! Choose another one.")
            warning = True


root = tk.Tk()
root.title("Password checker")
root.geometry('400x200')

tk.Label(root, text = 'Enter your password:',font =('Arial',12)).pack(pady = 10)
entry = tk.Entry(root, show = '*', width = 30)
entry.pack(pady = 5)
tk.Button(root, text = 'Check password', command = check_password).pack(pady = 10)
root.mainloop()
