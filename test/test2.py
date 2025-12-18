import win32print

printer_name = win32print.GetDefaultPrinter()
hPrinter = win32print.OpenPrinter("POS58")
print(printer_name)

try:
    hJob = win32print.StartDocPrinter(hPrinter, 1, ("Test", None, "RAW"))
    win32print.StartPagePrinter(hPrinter)

    win32print.WritePrinter(hPrinter, b"\n\n")
    win32print.WritePrinter(hPrinter, b"\n\n")
    win32print.WritePrinter(hPrinter, b"Hello POS Printer\n\n")
    win32print.WritePrinter(hPrinter,  str(hPrinter).encode())
    win32print.WritePrinter(hPrinter, b"\x1d\x56\x00")  # cut paper

    win32print.EndPagePrinter(hPrinter)
    win32print.EndDocPrinter(hPrinter)
finally:
    win32print.ClosePrinter(hPrinter)
