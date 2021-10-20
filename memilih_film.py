print("======================================================")
print("Selamat datang di bioskop abcdef")
print("Silahkan anda memilih genre film apa yang anda sukai")
print("======================================================")
nama = str(input("Masukkan Nama Anda anda \t: "))
umur = int(input("Masukkan Umur anda      \t: "))
print("======================================================")


##list
print("1. Action")
print("2. Horror")
print("3. Kartun")
print("======================================================")

#perintah input
pilihan = str(input("Masukkan Genre kesukaan anda \t: "))

if pilihan == '1':
    if umur >= 16:
        print("\nSilahkan anda memasukki studio satu untuk menonton film No Time To Die, Dan selamat menikmati filmnya")
    else:
        print("\nMaaf anda tidak bisa menonton No Time To Die karna tidak cukup umur, silahkan untuk memilih pilihan kategory kartun ")

elif pilihan == '2':
    if umur >= 16:
        print("\nSilahkan anda memasukki studio dua untuk menonton film The Medium, Dan selamat menikmati filmnya ")
    else:
        print("\nMaaf anda tidak bisa menonton No Time To Die karna tidak cukup umur, silahkan untuk memilih pilihan kategory kartun ")

elif pilihan == '3':
    if umur >= 5:
        print("\nSilahkan anda memasukki studio dua untuk menonton film Nussam, Dan selamat menikmati filmnya, Dan mohon untuk menjaga dan membimbing anak anda, dan terimakasih")