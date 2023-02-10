import json

import UtilFile
import UtilPython


def getJson(path):
    data = dict()

    try:
        with open(UtilFile.getPath(path), "r") as file:
            data = json.load(file)
    except:
        pass

    return data


def saveJson(path, new_data, overwrite=False):
    data = UtilPython.getByCondition(overwrite, dict(), dict(getJson(path).items()))

    for (key, value) in new_data.items():
        data[key] = value

    with open(UtilFile.getPath(path), "w") as file:
        file.write(json.dumps(data, indent=4))
