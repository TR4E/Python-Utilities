def getOrDefault(value, default_value):
    if value is not None:
        try:
            return value
        except Exception:
            pass

    return default_value


def getByCondition(condition, true_value, false_value):
    if condition:
        return true_value
    return false_value


def getClassName(clazz):
    return clazz.__class__.__name__.split(".")[-1]
