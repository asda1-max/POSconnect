import customtkinter as gui
from utils import printManager as PM

class appGui:

    def __init__(self):
        self.canvas = gui.CTk()
        self.canvas.geometry("500x500")
        self.canvas.title("konz")

        self.text1 = gui.CTkLabel(self.canvas, text="Print a test page", font=("arial", 40, "bold"))
        self.text1.pack(pady =(30,0))
        self.button1 = gui.CTkButton(self.canvas, command=PM.printThis,text="test print")
        self.button1.pack(pady = (30,0))
    
    def startGUI(self):
        self.canvas.mainloop()


app = appGui()
app.startGUI()