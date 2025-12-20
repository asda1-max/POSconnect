import view.mainGui as main
import control.printHandler as PM

PM.init_printer()

app = main.appGui()
app.geometry("1000x500")
app.title("woi")
app.startGUI()