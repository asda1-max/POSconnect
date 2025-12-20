import escpos.printer as printer

class setPrinter():
    def __init__(self, printer_name):
        """
        Docstring for __init__
        
        :param self: Description
        :param printer_name: Description
        """
        self.p = printer.Win32Raw(printer_name)

    def printConfigHelper(self):
        """
        Docstring for printConfigHelper
        
        :param self: Description
        """
        self.p.set()

    def printThis(self,title, text):
        """
        Docstring for printThis
        
        :param title: Description
        :param text: Description
        """
        try:
            self.p.open()
            self.p.text(title)
            self.p.text("\n\n=========================\n\n")
            self.p.text(text)
            self.p.cut() 
        finally:
            self.p.close()
