from model import printManager as PM
from tkinter import messagebox as MB

def printThis(title = "title 1",text="text"):
    if title.strip() == "" and text.strip() == "":
        MB.showerror(title="Error", message="Error Printing : \nTitle and Text are Empty, Make sure to atleast fill one field", icon="warning")
        return None
    try:
        PM.printThis(title, text)
        print("asu")
    except:
        print("Error, ")
        MB.showerror(title=None, message="Error Opening Printer")
        return "error"
