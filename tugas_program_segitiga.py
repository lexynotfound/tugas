import math


## Program Menghitung
p = 3.14

def _varname(name, nim, jrs, title):
    name = "Kurnia Raihan Ardian"
    nim = "2122.01.0018"
    jrs = "Sistem Informasi"
    title = "\tProgram Menghitung Segitiga"
    print("**" * len(title))
    print(title)
    print("**" * len(title))
    print("\t",name)
    print("\t",nim)
    print("\t",jrs)
    print("**" * len(title))
    return


def _judul():

    judul = "**"
    print("******************************" * (len(judul)))

##Memilih atau pilhan menu
def pilihan_():
    pilihan = ("1. Menghitung Segitiga", "2. Menghitung Lingkaran", "3. Menghitung Persegi Panjang", "4. Exit")
    print(pilihan[0])
    print(pilihan[1])
    print(pilihan[2])
    print(pilihan[3])

#memanggil atau menyurukan pengguna masukkan
def get_user_input():
    user_input = int(input("Masukkan Piilhan : " ))
    while user_input > 4 or user_input <= 0:
        print("Mohon untuk melakukan pilihan : ")
        user_input = int(input("Tolong di pilih : " ))

    else:
        return user_input
    


def segitiga(a, b, c):
    print("Menghitung Segitiga")
    #masukkan
    a = float(input(" Masukkan sisi A : "))
    b = float(input(" Masukkan sisi B : "))
    c = float(input(" Masukkan sisi C : "))
    #Menghitung Keliling
    keliling = a + b + c
    
    #Menghitung setangah keliling
    s = (a+b+c)/2
    
    #Menghitung Luas
    luas = math.sqrt(s*(s-a)*(s-b)*(s-c))

    print("\n Keliling segitiga adalah \t\t= %.2f" %keliling)
    print(" Setengah Keliling segitiga adalah  \t= %.2f" %s)
    print(" Luas Segitiga adalah \t\t\t= %0.2f" %luas)
    return a,b,c

## Menghitung persegi panjang
def _persegipanjang():

    print("\n Menghitung Persegi Panjang")
    panjang=float(input("Masukkan panjang \t ="))
    lebar=float(input("Masukkan lebar \t ="))

    luas = panjang * lebar
    keliling = 2 *(panjang*lebar)
    print("Luas adalah \t= ",str(luas))
    print("Keliling adalah \t= ",str(keliling))
    return


def _lingkaran():
    print("Menghitung Lingkaran")
    r = float(input(" Masukkan jari-jarinya = "))
    l = p*(r*r)
    k = 2*p*r
    print(" Hasilnya luas adalah     \t: ", str(l))
    print(" Hasilnya keliling adalah \t: ", str(k))
    return r

## kondisi
def tampilan_pilihan(index):

    ##Mengambil variable fungsi segitiga
    if index == 1:
        segitgita('a','b','c')
        return
    
    #mengambil variable fungsi lingkaran
    elif index == 2:
        _lingkaran()
        return
    
    #mengambil variable fungsi lingkaran
    elif index == 3:
        _persegipanjang()
        return
    
    #mengambil variable fungsi lingkaran
    elif index == 4:
        print("Terimakasih sudah mencoba program ini")
        return
    
    else:
        return user_input()



##menjadikan semua baris kode menjadi satu / memanggil
def main():
    _varname('name', 'nim', 'jrs', 'title')
    pilihan_()
    get_user_input()
    _judul()
    segitiga('a','b','c')
    _judul()
    _lingkaran()
    _judul()
    _persegipanjang()
    
main()