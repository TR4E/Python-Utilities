def log(prefix="", message="", variables=None):
    if prefix != "":
        prefix = prefix + "> "

    for variable in list(variables):
        message = message.replace("{}", str(variable), 1)

    print(prefix + message)
