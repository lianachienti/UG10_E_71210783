# Menu

suhu = float(input("Masukan suhu tubuh Anda : "))

# suhu rendah

if suhu <= 32:
    print("Anda kedinginan! Silahkan cari sesuatu yang hangat!")

# suhu normal
          
elif (suhu == 32) and (suhu < 37,6):
    print("Suhu Anda normal!")

# suhu tinggi

elif (suhu == 37,6) and (suhu <= 50):
    print("Anda demam! Jangan berpergian ke tempat fasilitas umum.")

# suhu tidak normal

else:
    print("Anda bukan manusia :)")
