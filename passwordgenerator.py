import random
import string

def password(length):

    a = string.ascii_letters
    d = string.digits
    s = string.punctuation

    all_chars = a + d + s

    p = [
        random.choice(a),
        random.choice(d),
        random.choice(s),
    ]
    p += random.choices(all_chars, k=length - len(p))
    random.shuffle(p)
    return ''.join(p)

try:
    length = int(input("Enter the desired password length (minimum 6): "))
    if length < 6:
        print("Password length should be at least 6.")
    else:
        p = password(length)
        print(f"Your secure password is: {p}")
except ValueError:
    print("Please enter a valid number.")