import random
import string
import re


def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))


def is_valid_login(login):
    if re.match(r"[^@]+@[^@]+\.[^@]+", login):
        return True
    elif re.match(r"^\+?[1-9]\d{1,14}$", login):
        return True
    else:
        return False