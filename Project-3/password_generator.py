import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    try:
        user_input = input("Password length [default 12]: ").strip()
    except EOFError:
        user_input = "12"
    try:
        length = int(user_input) if user_input else 12
    except ValueError:
        length = 12
    print("Generated password:", generate_password(length))

if __name__ == "__main__":
    main()