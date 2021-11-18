daftar = ((input("Masukkan daftar siswa :")))
print ("Dafar siswa :", daftar.title().split(","))
add = ((input("Masukan siswa yang ingin ditambahkan :")))

if add not in daftar :
    print ("Hasil penambahan pada daftar siswa :", [daftar.title(), add.upper()])
else :
    print("Siswa atas nama", (add.upper()), "sudah berada dalam daftar siswa")
