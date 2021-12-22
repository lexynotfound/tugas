import datetime as dt
import math
from datetime import datetime
import qrcode

## Display atau menampilkan nama

## menentukan tipe kendaraan
def tipe_kendaraan():
    title = "* Selamat datang di Parkiran AR *"
    print("*" * len(title))
    print(title)
    print("*" * len(title))

    tipe_kendaraan = str(input("Pilih jenis kendaraaan anda : \n \t \n 1. Mobil \t \n 2. Motor \n\nMasukkan tipe kendaraan anda :"))
    print("*****")
    jam_masuk = str(datetime.now())[11:19]
    jam_keluar = str(datetime.now())[11:19]


    if tipe_kendaraan == "1" or tipe_kendaraan == "Mobil, MOBIL, mobil":
        lama_parkir = jam_masuk
        biaya_parkir = 10000

        #biaya_parkir = +5000-5000+(biaya_parkir * lama_parkir + 5000)
        print("*****")
        print("Mulai Parkir Mobil Pukul :", lama_parkir )
        print("Biaya Parkir Mobil  :  Rp.", biaya_parkir)
        print("*****")

    elif tipe_kendaraan == "2" or tipe_kendaraan == "Motor, motor, MOTOR":
        lama_parkir = jam_masuk
        biaya_parkir_motor = 5000

        print("*****")
        print("Mulai Parkir Motor Pukul :", lama_parkir)
        print("Biaya Parkir Motor  :  Rp.", biaya_parkir_motor)
        print("*****")

def tipe_qrcode():
    biaya_parkir = 10000
    jam_masuk = str(datetime.now())[11:19]
    
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=15,
        border=5
    )
    data = "Jam Masuk : ", jam_masuk, " Biaya Parkir : ", biaya_parkir
    qr.add_data(data)
    qr.make()
    img = qr.make_image(fill='black', back_color='white')
    type(img)
    img.save('Struk Parkir.png')
    

tipe_kendaraan()
tipe_qrcode()