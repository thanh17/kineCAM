import cups
conn = cups.Connection()
printers = conn.getPrinters()
printer_name = list(printers.keys())[-1]
print(printer_name)
conn.printFile(printer_name,'/usr/share/raspberrypi-artwork/raspberry-pi-logo.png', "Hello",{}) 
