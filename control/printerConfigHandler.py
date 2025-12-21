import model.printerConfigManager as PCM

def loadConfig():
    try:
        data = PCM.loadConfig()
    except:
        return "Error getting printer name"
    return data

def saveConfig(data):
    try:
        PCM.saveConfig(data)
    except:
        return "Error"
    return "saved"

    