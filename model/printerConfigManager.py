import json

def loadConfig():
    with open('printerConfig.json', 'r') as configFile :
        data = json.load(configFile)
        return data

def saveConfig(data):
    with open('printerConfig.json', 'w') as configFile :
        json.dump(data,configFile)

