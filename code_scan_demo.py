# simple_ghas_demo.py

import hashlib

def insecure_hashing(password):
    """
    This function uses MD5 hashing, which is considered insecure.
    It is intentionally added here to demonstrate a GitHub Advanced Security alert.
    """
    hashed_password = hashlib.md5(password.encode()).hexdigest()  # MD5 is insecure
    print(f"Your hashed password is: {hashed_password}")

if __name__ == "__main__":
    user_password = input("Enter your password: ")
    insecure_hashing(user_password)
