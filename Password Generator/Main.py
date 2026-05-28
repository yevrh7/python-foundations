import random
import string

print("--- Password Generator & Checker ---")

choice = 0

while choice != 3:
    print("1. Generate a Password")
    print("2. Check Password Strength")
    print("3. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        password = []
        chars = list(string.ascii_lowercase)
        
        pw_len = int(input("Enter preffered password length: "))
        up = input("Include uppercase letters? (y/n): ")
        num = input("Include numbers? (y/n): ")
        sp = input("Include special characters? (y/n): ")
        
        if up == "y":
            chars.extend(list(string.ascii_uppercase))
        
        if num == "y":
            chars.extend(list(string.digits))
            
        if sp == "y":
            chars.extend(list(string.punctuation))
        
        while len(password) < pw_len:
            password.append(random.choice(chars))
            
        print("Generated Password")
        print("".join(password))
            
    elif choice == 2:
        password_strength = ""
        password1 = input("Enter password to check: ")
        
        has_upper = any(char.isupper() for char in password1)
        has_digits = any(char.isdigit() for char in password1)
        has_sp = any(not char.isalnum() for char in password1)
            
        if len(password1) < 8:
            password_strength = "Weak"
            
        elif has_upper == True and has_digits == True and has_sp == True and len(password1) >= 12:
            password_strength = "Strong"

        elif has_upper == True and has_digits == True and has_sp == True and len(password1) >= 8:
            password_strength = "Medium"
            
        print(password_strength)
    
    elif choice == 3:
        print("Exiting...")
        break