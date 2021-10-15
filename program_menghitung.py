import math


##phi
p = 3.14


def variable_data_1(): ### sebuah fungsi
    print("\n")
    print("Nama     \t= Kurnia Raihan Ardian")
    print("NIM      \t= 2122.01.0018")
    print("Jurusan  \t= SISTEM INFORMASI")
    print("Instagram \t= raihanardila\n")

def _display():
    judul = "** Menghitung Program **"
    print("*" * len(judul))
    print(judul)
    print("*" * len(judul))


variable_data_1()
_display()


## MenuList
print("1. Menghitung Lingkaran")
print("2. Menghitung Persegi")
print("3. Exit")

pilihan = input("Masukkan pilihan : ")

if pilihan == '1' :
    pilihan = float(input("Masukkan jari-jarinya = "))
    l = p*(pilihan*pilihan)
    k = 2*p*pilihan
    print("Hasilnya luas adalah     \t: ", str(l))
    print("Hasilnya keliling adalah \t: ", str(k))

elif pilihan == '2':
    panjang=float(input("Masukkan panjang \t ="))
    lebar=float(input("Masukkan lebar \t ="))

    luas = panjang * lebar
    keliling = 2 *(panjang*lebar)

    print("\nLuas Persegi Panjang   \t: ",str(luas))
    print("Keliling Persegi Panjang \t: ",str(keliling))
