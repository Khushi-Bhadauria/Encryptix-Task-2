import random
import string

length = int(input("Enter desired password length: "))
characters = string.ascii_letters + string.digits
password = ''.join(random.choice(characters) for _ in range(length))
print("Generated Password:", password)
