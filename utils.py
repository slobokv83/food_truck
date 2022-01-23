import json


def loadJson():
    with open('userInput.json') as json_file:
        data = json.load(json_file)
        return data
