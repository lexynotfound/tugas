## UTS MEMBUAT APLIKAI PARKIR##
## NAMA : KURNIA RAIHAN ARDIAN##
## NIM : 2122.01.0018##
## PRODI : SISTEM INFORMASI##
## KAMPUS : IDS##


import datetime as dt
import math

## Display atau menampilkan nama
def display_intro():
    title = "** Selamat datang di Parkiran AR **"
    print("*" * len(title))
    print(title)
    print("*" * len(title))

## menentukan tipe kendaraan
def tipe_kendaraan():
    tipe_kendaraan = str(input("Pilih jenis kendaraaan anda : \n \t \n 1. Mobil \t \n 2. Motor \n\nMasukkan tipe kendaraan anda :"))
    print("***********************************")
    jam_masuk = int(input(" Masukkan Jam Masuk \t: "))
    jam_keluar = int(input(" Masukkan Jam Keluar \t: "))
    

    if tipe_kendaraan == "1" or tipe_kendaraan == "Mobil, MOBIL, mobil":
        lama_parkir = jam_keluar - jam_masuk
        biaya_parkir = 10000

        if (biaya_parkir >= lama_parkir):
            biaya_parkir = +5000-5000+(biaya_parkir * lama_parkir + 5000)
            print("***********************************")
            print("Lama Parkir Mobil   : ", lama_parkir, "jam\n")
            print("Biaya Parkir Mobil  :  Rp.", biaya_parkir)
            print("***********************************")
            print("***********************************")
            print("Lama Parkir Mobil   : ", lama_parkir, "jam\n")
            print("Biaya Parkir Mobil  :  Rp.", biaya_parkir)
            print("***********************************")

    elif tipe_kendaraan == "2" or tipe_kendaraan == "Motor, motor, MOTOR":
        lama_parkir = jam_keluar - jam_masuk
        biaya_parkir_motor = 5000

        if (biaya_parkir_motor >= lama_parkir):
            biaya_parkir_motor = (biaya_parkir_motor * lama_parkir)

            print("***********************************")
            print("Lama Parkir Motor   : ", lama_parkir, "jam\n")
            print("Biaya Parkir Motor  :  Rp.", biaya_parkir_motor)
            print("***********************************")
            print("***********************************")
            print("Lama Parkir Motor   : ", lama_parkir, "jam\n")
            print("Biaya Parkir Motor  :  Rp.", biaya_parkir_motor)
            print("***********************************")


display_intro()
tipe_kendaraan()
