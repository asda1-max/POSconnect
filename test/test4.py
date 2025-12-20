import escpos.printer as printers

printer = printers.Win32Raw("POS58")
printer.open()

# TITLE
printer.set(align="center", bold=True)
printer._raw(b'\x1d\x21\x22')  # DOUBLE HEIGHT + WIDTH
printer.text("aaaaaaaaaaaaaaaaaaaaaaaaaaaaa" + "\n")

# RESET FONT
printer._raw(b'\x1d\x21\x00')

# BODY
printer.text("\n=========================\n\n")
printer.text("bbbbbbbbbbbbbb" +"\n\n\n")

printer.close()