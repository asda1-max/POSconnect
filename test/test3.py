import escpos.printer as printer

# Ganti 'your_printer_name' dengan nama printer Anda di Windows (misalnya, 'Epson TM-T82')
# Anda bisa melihat nama printer di 'Settings > Devices > Printers & Scanners'
p = printer.Win32Raw(printer_name='POS58')

try:
    p.image(img_source="asu.png", fragment_height=100)
    p.open()
    p.text("Halo Dunia!\n")
    p.text("Ini adalah cetakan uji dari Python.\n")
    p.cut() # Perintah potong kertas (jika printer mendukung)
finally:
    p.close()
