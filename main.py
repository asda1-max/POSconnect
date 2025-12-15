import customtkinter as gui
from utils import printManager as PM


    
class appGui(gui.CTk):
    """
    GUI Manager Class
    """

    def __init__(self):
        """
        GUI initialization
        """
        super().__init__()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.mainFrame = gui.CTkFrame(self)
        self.mainFrame.grid_columnconfigure(0,weight=1)
        self.mainFrame.grid_rowconfigure(0, weight= 0)

        self.textBoxFrame = gui.CTkFrame(self.mainFrame)
        self.textBoxFrame.grid_columnconfigure(0,weight=1)
        self.textBoxFrame.grid_rowconfigure(0, weight= 0)

        self.title = gui.CTkLabel(self.mainFrame, text="POS-CONNECT!", height= 30, font=("arial", 40, "bold"))

        self.label1 = gui.CTkLabel(self.textBoxFrame, text="Title :")
        self.textbox1  = gui.CTkTextbox(self.textBoxFrame, height=50, width=300)
        self.label2 = gui.CTkLabel(self.textBoxFrame, text="Text :")
        self.textbox2  = gui.CTkTextbox(self.textBoxFrame,height=100, width=300)

        self.button1 = gui.CTkButton(self.mainFrame, command=self.openprint,text="Print!")

        self.mainFrame.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 2, rowspan = 2, padx = 20, pady = 20)

        self.title.grid(row = 0, column = 0, sticky = "EW", pady = (30,30), columnspan =2)

        self.textBoxFrame.grid(row = 1,sticky = "NSEW", padx = 30)

        self.label1.grid(row = 1, column = 0, pady = 20, padx = 10)
        self.textbox1.grid(row = 1, column = 1, pady = 20,padx = 10)
        self.label2.grid(row = 2, column =0 , pady = 20,padx = 10)
        self.textbox2.grid(row = 2, column = 1, pady = 20,padx = 10)

        self.button1.grid(row = 3, column = 0, sticky ="EW", pady = (20,0),padx = 20, columnspan =4)
    
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

        self.text1 = self.textbox1.delete("0.0", "end")
        self.text2 = self.textbox2.delete("0.0", "end")
        


app = appGui()
app.geometry("600x500")
app.startGUI()