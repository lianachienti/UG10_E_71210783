#input data
daftar = ((input("Masukkan daftar siswa :")))
print ("Dafar siswa :", daftar.title().split(","))

#add data
add = ((input("Masukan siswa yang ingin ditambahkan :")))

#hasil akhir
if add not in daftar :
    print ("Hasil penambahan pada daftar siswa :", [daftar.title(), add.upper()])
else :
    print("Siswa atas nama", (add.upper()), "sudah berada dalam daftar siswa")
