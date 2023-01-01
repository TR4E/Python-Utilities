def getCharacterAtIndex(string, index):
    try:
        return string[index]
    except:
        return ""


def cleanString(string):
    string = string.lower()
    string = string.replace("_", " ")

    builder = ""

    for (index, character) in enumerate(string):
        lastCharacter = getCharacterAtIndex(string, index - 1)

        if index == 0 or lastCharacter == " ":
            character = character.upper()

        builder += character

    return builder


def sliceString(string):
    for character in ["_", " "]:
        string = string.replace(character, "")

    return string


def trimString(string, endIndex):
    if len(string) > endIndex:
        string = string[:endIndex]

    return string
