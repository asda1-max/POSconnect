import model.printerConfigManager as PCM
import tkinter.messagebox as MB

def loadConfig():
    try:
        data = PCM.loadConfig()
    except:
        MB.showerror(title="Error", message="Error loading config",icon="error")
    return data

def saveConfig(data):
    try:
        PCM.saveConfig(data)
    except:
        MB.showerror(title="Error", message="Error Saving config",icon="error")
        return "Error"
    MB.showinfo(title="Success", message="Config Saved!",icon="info")

    