## UTS MEMBUAT APLIKAI MENGHITUNG NILAI##
## NAMA : KURNIA RAIHAN ARDIAN##
## NIM : 2122.01.0018##
## PRODI : SISTEM INFORMASI##
## KAMPUS : IDS##

#Identitas mahasiswa
nama = input("Nama : ")
nim = int(input("NIM : "))
prodi = str(input("PRODI : "))

#deklarasi fungsi operator
def fungsi_total_nilai (nilai_Tugas, nilai_UTS,nilai_UAS):
    nilai_Tugas = int(nilai_Tugas) * 0.2
    nilai_UTS = int(nilai_UTS) * 0.3
    nilai_UAS = int(nilai_UAS) * 0.5
    nilai_akhir = nilai_Tugas + nilai_UTS + nilai_UAS
    return nilai_akhir

##fungsi percabangan
def fungsi_percabangan(var_nilai):
    var_index = ""
    if (var_nilai >= 0 and var_nilai < 20):
        var_index = "E"
    elif (var_nilai >= 20 and var_nilai < 40):
        var_index = "D"
    elif (var_nilai >= 40 and var_nilai < 60):
        var_index = "C"
    elif (var_nilai >= 60 and var_nilai < 80):
        var_index = "B"
    if (var_nilai >= 80 and var_nilai < 100):
        var_index = "A"
    return var_index

##perulangan
def perulangan():
    var_hasil_perulangan = 0
    for i in range (1,3):
        print("====Nilai ke ===== " , i, "===========")
        var_Tugas = input("Nilai Tugas \t: ")
        var_UTS = input("Nilai UTS \t: ")
        var_UAS = input("Nilai UAS \t: ")

        #pemanggilan fungsi penjumlahan
        var_hasil_perulangan += (int(fungsi_total_nilai(var_Tugas,var_UTS,var_UAS)))
        return var_hasil_perulangan / i
## pemanggilan perualngan
var_total = perulangan()

print("============= TOtal Nilai============")
print("total nilai akhir yang didapat adalah : ",var_total )

##pemanggialan percabangan
print("total nilai akhir yang didapat adalah : ",fungsi_percabangan(var_total) )
