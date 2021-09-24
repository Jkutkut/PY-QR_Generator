#!/usr/bin/env python3

from Classes.qr import QR

def spectedQR(text):
    import qrcode
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save("qr_spected.png")

if __name__ == "__main__":
    text = 'HELLO WORLD'
    # qrCode = QR(text)
    spectedQR(text)
    
    
    
    print("Thanks for using this code, I hope you liked it.")
    print("See more projects like this one on https://github.com/jkutkut/")
