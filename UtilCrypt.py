import hashlib


def hash(string, amount=1, pepper=None):
    if pepper is not None:
        string = pepper + "$" + string

    print(string)

    for i in range(amount):
        string = hashlib.sha512(bytes(string, "UTF-8")).hexdigest()

    return string
