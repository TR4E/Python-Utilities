import base64

from cryptography.fernet import Fernet


def generate_key(key):
    result = key

    while len(result) < 32:
        result += "X"

    return base64.urlsafe_b64encode(result.encode())


def encrypt(key, string, amount):
    result = string

    for i in range(amount):
        cipher = Fernet(generate_key("{}:{}".format(amount, key)))

        result = cipher.encrypt(result.encode()).decode("UTF-8")

    return result


def decrypt(key, string, amount):
    result = string

    for i in range(amount):
        cipher = Fernet(generate_key("{}:{}".format(amount, key)))

        result = cipher.decrypt(result).decode("UTF-8")

    return result
