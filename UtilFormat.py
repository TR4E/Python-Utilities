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


def unSliceString(string):
    string = string.replace("_", " ")

    builder = ""

    for (index, character) in enumerate(string):
        lastCharacter = getCharacterAtIndex(string, index - 1)
        nextCharacter = getCharacterAtIndex(string, index + 1)

        if index == 0 or lastCharacter == " ":
            character = character.upper()

        builder += character

        conditions = [
            not character == character.upper(),
            nextCharacter == nextCharacter.upper(),
            index < string.length() - 1
        ]

        if all(conditions):
            builder += " "

    return builder


def trimString(string, endIndex):
    if len(string) > endIndex:
        string = string[:endIndex]

    return string
