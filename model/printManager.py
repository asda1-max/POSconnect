import escpos.printer as printer

class setPrinter():
    def __init__(self, printer_name):
        """
        Docstring for __init__
        
        :param self: Description
        :param printer_name: Description
        """
        self.p = printer.Win32Raw(printer_name)

    def setFontHuge(self):
        self.p._raw(b'\x1d\x21\x22')

    def setFontSmall(self):
        self.p._raw(b'\x1d\x21\x00')
        

    def printThis(self,title, text):
        """
        Docstring for printThis
        
        :param title: Description
        :param text: Description
        """
        try:
            self.p.open()
            self.setFontSmall()
            self.p.text("\n\n\n\n================================\n\n")
            self.setFontHuge()
            self.p.set(align="center", bold=True)
            self.setFontHuge()
            self.p.text(title)
            self.p.set(align="left", bold=False)
            self.setFontSmall()
            self.p.text("\n\n================================\n\n")
            self.p.text(text)
            self.p.text("\n\n================================\n\n")
        finally:
            self.p.close()
