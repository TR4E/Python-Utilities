def log(prefix="", message="", variables=None):
    if prefix != "":
        prefix = prefix + "> "

    if variables is not None:
        for variable in list(variables):
            message = message.replace("<var>", str(variable), 1)

    print(prefix + message)
