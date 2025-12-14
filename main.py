import customtkinter as gui
from utils import printManager as PM


    
class appGui(gui.CTk):
    """
    Gui Manager Class
    """

    def __init__(self):
        super().__init__()
        self.title = gui.CTkLabel(self, text="Print a test page", font=("arial", 40, "bold"))
        self.textbox1  = gui.CTkTextbox(self, height=50)
        self.textbox2  = gui.CTkTextbox(self)
        self.button1 = gui.CTkButton(self, command=self.openprint,text="test print")

        self.title.pack(pady =(30,0))
        self.textbox1.pack(pady =(30,0))
        self.textbox2.pack(pady =(30,0))
        self.button1.pack(pady = (30,0))
    
    def startGUI(self):
        """
        Start the GUI
        """
        self.mainloop()

    def openprint(self):
        """
        print anything in the text box
        """
        self.text1 = self.textbox1.get("0.0", "end")
        self.text2 = self.textbox2.get("0.0", "end")
        PM.printThis(self.text1, self.text2)
        


app = appGui()
app.geometry("600x500")
app.startGUI()