# Kalkulator Akar dan Pangkat

# Menu
print("==== Kalkulator Akar dan Pangkat ====")
print("Pilihan Menu :")
print("1. Pangkat 2 (Kuadrat)")
print("2. Pangkat 3 (Kubik)")
print("3. Akar Kuadrat")

# Pilihan
opsi = input("Masukan menu yang anda pilih : ")

# opsi 1
if opsi == '1' :
    a1 = int(input("Masukan bilangan yang ingin di pangkatkan : "))
    a2 = int(2)
    print("Hasil dari pemangkatan" , a1 , "dengan 2 (Pangkat) adalah : " , pow(a1 , a2))

# opsi 2
if opsi == '2' :
    a1 = int(input("Masukan bilangan yang ingin dipangkatkan : "))
    a2 = int(3)
    print("Hasil dari pemangkatan" , a1 , "dengan 3 (Kubik) adalah : " , pow(a1, a2))

#opsi 3
if opsi == '3' :
   a1 = int(input("Masukan bilangan yang ingin diakarkan : "))
   print("Hasil akar kuadrat dari bilanag" , a1 , "adalah : " , pow(a1,1/2))

#opsi 4
else :
       print("Pilihan menu yang dimasukkan tidak sesuai!")
