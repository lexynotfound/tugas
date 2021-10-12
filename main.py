## Membuat sebuah projek program kalkulator
import math #menggunakan library matematika
#from ctypes import c_float #menggunakan sebuah library tipe data Bahasa C/C++ 

## Membuat sebuah nilai variable luas lingkaran
p = 3.14

##nilai skor





def variable_data_1(): ### sebuah fungsi
    print("\n")
    print("Nama\t = Kurnia Raihan Ardian")
    print("NIM\t = 2122.01.0018")
    print("Jurusan\t = SISTEM INFORMASI")
    print("Instagram\t = __xiaoyie")

print("========================================================")
print("Sebelum Masuk kedalam permainan harap masukkan namamu!")
print("========================================================")

variable_name = input("Masukkan Nama =\t ")
variable_age = int(input("Masukkan Umur =\t "))



print("\nNama",variable_name,"umur", +variable_age,"tahun","\nSelamat Datang","Di percobaan program pertama saya di python ini :)\n")
#luas lingkaran
r=float(input("Masukkan jari-jari \t="))
l = p*(r*r)
k = 2*p*r
print("Luas lingakran \t= ", l)
print("Keliling \t= ", k)
print("\n\n")

## persegi panjang

panjang=float(input("Masukkan panjang =\t"))
lebar=float(input("Masukkan lebar =\t"))

luas = panjang * lebar
keliling = 2 *(panjang*lebar)

print("\nLuas Persegi Panjang \t\t:",luas)
print("Keliling Persegi Panjang\t:",keliling)

pertanyaan = input("Apakah anda ingin bermain sebentar?, Y/T\n")

#Membuat pilihan
## menunujukkan sebuah nilai Y/N
if pertanyaan == 'Y' or pertanyaan == 'y':
    print("\nSelamat Bermain\n")
## permainan tanya jawab
    print("Jika jari-jari bernilai 5.4, hitunglah kelilingnya, = \t")
    skor = 15
    total_skor = skor
    jawaban=input()
    if jawaban == '91.562':
        skor = skor+10 
        print("jawabannya adalah =\t ", jawaban)
        print("nilai anda adalah =\t ",skor)
        print(variable_data_1())


    else:
        print("Jawaban anda salah")
        skor = skor-5
        print("nilai anda sekarang adalah = ", skor)

elif pertanyaan == 'T' or pertanyaan == 't':
    print("\nMaaf anda tidak bisa melanjutkan permainan ini terimakasih\n")

## Membuat sebuah pertanyaan kepada pengguna program
