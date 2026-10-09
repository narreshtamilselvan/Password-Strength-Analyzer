
import re

password = input("Enter your password: ")

if len(password) < 8:
    print("Weak Password")
    print("Password must contain at least 8 characters.")

elif not re.search("[A-Z]", password):
    print("Weak Password")
    print("Add at least one uppercase letter.")

elif not re.search("[a-z]", password):
    print("Weak Password")
    print("Add at least one lowercase letter.")

elif not re.search("[0-9]", password):
    print("Weak Password")
    print("Add at least one number.")

elif not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
    print("Weak Password")
    print("Add at least one special character.")

else:
    print("Strong Password!")
