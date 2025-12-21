import json
import os.path

def loadConfig():
    if os.path.exists("./printerConfig.json"):
        with open('printerConfig.json', 'r') as configFile :
            data = json.load(configFile)
            return data
    else:
        saveConfig("POS58")

def saveConfig(data):
    with open('printerConfig.json', 'w') as configFile :
        json.dump(data,configFile)

