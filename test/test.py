from win32printing import Printer

font = {
    "height": 20,
    "weight" : 1,
    "underline" : 30
    }
with Printer(linegap=1,printer_name="POS58") as printer:
    printer.text("      title1      ", font_config=font)
    printer.text("title2", font_config=font)
    printer.text("title3", font_config=font)
    printer.text("title4", font_config=font)
    printer.new_page()
