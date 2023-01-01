import os
import sys

ROOT_PATH = "" if "linux" in sys.platform else (sys.path[1] + "\\")


def getPath(path):
    path = path.replace("/", "\\")

    tokens = path.rsplit("\\", 1)

    folder_path = ROOT_PATH + tokens[0]

    if "\\" in path and not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = folder_path + "\\" + tokens[1]

    if not os.path.exists(file_path):
        open(file_path, "w")

    return file_path


def getLines(path):
    lines = []

    with open(getPath(path), "r") as file:
        for line in file:
            lines.append(line.strip())

    return lines
