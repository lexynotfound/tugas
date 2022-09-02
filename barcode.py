from codecs import unicode_escape_decode
import os
from tokenize import String
import unicodedata
import pyqrcode
import png
from PIL import Image


class QR_GENERATOR(object):
    def __init__(self, text):
        self.qr_image = self.qr_generator(text)

    @staticmethod
    def qr_generator(text):
        qr_code = pyqrcode.create(text)
        file_name = "Barcode Pembayaran"
        save_path = os.path.join(os.path.expanduser('~'),'Pictures')
        print("Gambar disimpan: ", save_path)
        name = f"{save_path}\{file_name}.png"
        qr_code.png(name, scale=10)
        image = Image.open(name)
        image = image.resize((400, 400), Image.ANTIALIAS)
        image.show()


if __name__ == "__main__":
    QR_GENERATOR(input("Masukkan text atau link: "))
