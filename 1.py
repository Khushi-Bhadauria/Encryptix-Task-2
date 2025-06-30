import random
import string

length = int(input("Enter desired password length: "))
password = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
print("Generated Password:", password)
