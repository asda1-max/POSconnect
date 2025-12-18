import customtkinter as gui
import time
from utils import printManager as PM

class ToplevelWindow(gui.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = gui.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)
    
class appGui(gui.CTk):
    """
    GUI Manager Class
    """

    def __init__(self, *args, **kwargs):
        """
        GUI initialization
        """
        super().__init__(*args, **kwargs)
        self.toplevel_window = None
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.mainFrame = gui.CTkFrame(self)
        self.mainFrame.grid_columnconfigure(0,weight=1)
        self.mainFrame.grid_rowconfigure(0, weight= 1)

        self.optionFrame = gui.CTkFrame(self)
        self.optionFrame.grid_columnconfigure(0,weight=1)
        self.optionFrame.grid_rowconfigure(0, weight= 0)

        self.textBoxPane = gui.CTkFrame(self.mainFrame)
        self.textBoxPane.grid_columnconfigure(0,weight=1)
        self.textBoxPane.grid_rowconfigure(0, weight= 1)

        self.radioButtonPane = gui.CTkFrame(self.optionFrame)
        self.radioButtonPane.grid_columnconfigure(0,weight=1)
        self.radioButtonPane.grid_rowconfigure(0, weight= 0)

        self.titleLable = gui.CTkLabel(self.mainFrame, text="POS-CONNECT!", height= 30, font=("arial", 40, "bold"))

        self.label1 = gui.CTkLabel(self.textBoxPane, text="Title :")
        self.textbox1  = gui.CTkTextbox(self.textBoxPane, height=50, width=500)
        self.label2 = gui.CTkLabel(self.textBoxPane, text="Text :")
        self.textbox2  = gui.CTkTextbox(self.textBoxPane,height=100, width=500)

        self.button1 = gui.CTkButton(self.mainFrame, command=self.openprint,text="Print!")

        self.radPaneTitle = gui.CTkLabel(self.optionFrame, text ="Templates : ", font=("arial", 20))
        self.radButton1 = gui.CTkButton(self.radioButtonPane,text="Task", command=self.setTask)
        self.radButton2 = gui.CTkButton(self.radioButtonPane,text="Project", command=self.setProject)
        self.radButton3 = gui.CTkButton(self.radioButtonPane,text="Big Project",command=self.setBigProject)
        self.labelAdvOption = gui.CTkLabel(self.optionFrame, text ="Advanced Settings : ", font=("arial", 20) )
        self.advOptionButton = gui.CTkButton(self.optionFrame, text ="Font Settings",command=self.open_toplevel)

        self.mainFrame.grid(row = 0, column = 0, sticky = "NSEW", rowspan = 2, padx = 20, pady = 20)
        self.optionFrame.grid(row = 0, column = 1, sticky = "NSEW", rowspan = 2, padx = (0,20), pady = 20)
        self.radioButtonPane.grid(row = 1, column = 0, sticky = "NSEW", rowspan = 2, padx = 20, pady = 20)

        self.titleLable.grid(row = 0, column = 0, sticky = "EW", pady = (30,30), columnspan =2)

        self.textBoxPane.grid(row = 1,sticky = "NSEW", padx = 30)

        self.label1.grid(row = 1, column = 0, pady = 20, padx = 10)
        self.textbox1.grid(row = 1, column = 1, pady = 20,padx = 10)
        self.label2.grid(row = 2, column =0 , pady = 20,padx = 10)
        self.textbox2.grid(row = 2, column = 1, pady = 20,padx = 10)

        self.button1.grid(row = 3, column = 0, sticky ="EW", pady = (20,20),padx = 20, columnspan =2)

        self.radPaneTitle.grid(row = 0, column = 0, sticky = "EW", pady = (50,0))
        self.radButton1.grid(row = 0, padx = 30,pady = (40,0))
        self.radButton2.grid(row = 1, padx = 30,pady = (20,0))
        self.radButton3.grid(row = 2, padx = 30,pady = (20,40))
        self.labelAdvOption.grid(row = 3,column = 0, sticky= "NSEW", pady = 20, padx = 20)
        self.advOptionButton.grid(row = 4,column = 0, sticky = "NSEW", pady = (0,20), padx = 20)
        
    
    def startGUI(self):
        """
        Start the GUI
        """
        self.mainloop()

    def resetTextBox(self):
        self.text1 = self.textbox1.delete("0.0", "end")
        self.text2 = self.textbox2.delete("0.0", "end")

    def openprint(self):
        """
        print anything in the text box
        """
        self.text1 = self.textbox1.get("0.0", "end")
        self.text2 = self.textbox2.get("0.0", "end")

        PM.printThis(self.text1, self.text2)
        self.resetTextBox()
    
    def setTask(self):
        self.resetTextBox()
        self.textbox1.insert("0.0", "Your Task")
    
    def setProject(self):
        self.resetTextBox()
        self.textbox1.insert("0.0", "Your Project")
    
    def setBigProject(self):
        self.resetTextBox()
        self.textbox1.insert("0.0", "BIG PROJECT !")

    def open_toplevel(self):
        
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
            self.toplevel_window.after(100, self.toplevel_window.focus)
        else:
            self.toplevel_window.focus()  # if window exists focus it
