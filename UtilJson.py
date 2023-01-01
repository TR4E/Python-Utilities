import json

import UtilFile


def getJson(path):
    data = dict()

    try:
        with open(UtilFile.getPath(path), "r") as file:
            data = json.load(file)
    except:
        pass

    return data


def saveJson(path, new_data, overwrite=False):
    data = dict()
    if overwrite:
        data = dict(getJson(path).items())

    for (key, value) in new_data.items():
        data[key] = value

    with open(UtilFile.getPath(path), "w") as file:
        file.write(json.dumps(data, indent=4))
