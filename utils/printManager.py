from win32printing import Printer

print("loadded")

def printThis(title = "title 1",text="text"):
    font = {
        "height": 9,
        "weight" : 800,
        "underline" : 30
        }
    fontTitle = {
        "height": 20,
        "weight" : 1,
        "underline" : 30
        }
    with Printer(linegap=1,printer_name="POS58") as printer:
        printer.text(title, font_config=fontTitle)
        printer.text(text, font_config=font)

        printer.new_page()
        print("woi")
