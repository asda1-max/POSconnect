from win32printing import Printer

print("loaded")
def printThis(title = "title 1",text="text"):
    font = {
        "height": 14,
        "weight" : 1,
        "underline" : 0
        }
    fontTitle = {
        "height": 18,
        "weight" : 800,
        "underline" : 0
        }
    margin = {
        "height" : 50
    }
    with Printer(linegap=1,printer_name="POS58") as printer:
        printer.text(" " * 5, font_config=font)
        printer.start_page()
        printer.text("==============================",font_config=font)
        printer.text(" ",font_config=font)
        printer.text(title, font_config=fontTitle,align="center")
        printer.text("==============================",font_config=font)
        printer.text(text, font_config=font)

        printer.new_page()

