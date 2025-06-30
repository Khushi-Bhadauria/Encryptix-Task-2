import random
import string

length = int(input("Enter password length (min 4): "))

if length < 4:
    print("Password length too short for secure password!")
else:
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password += [random.choice(all_chars) for _ in range(length - 4)]
    random.shuffle(password)
    print("Generated Password:", ''.join(password))
