import tkinter as tk
from tkinter import filedialog
import pyqrcode
from pyqrcode import QRCode

# func
def createQR():
    url = qr_label.get()

    if url:
        qr_url = pyqrcode.create(url)
        file_dialog = filedialog.asksaveasfilename(defaultextension=".svg", filetypes=[("SVG Dosyaları","*.svg")])

        if qr_url:
            qr_url.svg(file_dialog, scale=8)
            status_label.config(text="QR Oluşturuldu ve Kaydedildi.")

# GUI
app_window = tk.Tk()
app_window.title("QR Generator")
app_window.resizable(0,0)


url_label = tk.Label(app_window, text="URL Girin: ")
qr_label = tk.Entry(app_window, width=40)
qr_code_button = tk.Button(app_window, text="QR Generate", command=createQR)
status_label = tk.Label(app_window, text="")

url_label.grid(row=0,column=0,padx=10,pady=10)
qr_label.grid(row=0,column=1,padx=10,pady=10)
qr_code_button.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
status_label.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

app_window.mainloop()