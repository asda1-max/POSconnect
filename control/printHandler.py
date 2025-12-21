import control.printerConfigHandler as PCH
from model import printManager as PM
from tkinter import messagebox as MB


printer = None

def init_printer(printer_name = PCH.loadConfig()):
    """
    Docstring for init_printer
    
    :param printer_name: Your printer name
    """
    global printer
    printer = PM.setPrinter(printer_name)

def printThis(title = "title 1",text="text"):
    """
    Docstring for printThis
    
    :param title: Title
    :param text: Text
    """
    if title.strip() == "" and text.strip() == "":
        MB.showerror(title="Error", message="Error Printing : \nTitle and Text are Empty, Make sure to atleast fill one field", icon="error")
        return None
    try:
        printer.printThis(title, text)
        print("asu")
    except:
        print("Error, ")
        MB.showerror(title="Error", message="Error Opening Printer",icon="error")
        return "error"
