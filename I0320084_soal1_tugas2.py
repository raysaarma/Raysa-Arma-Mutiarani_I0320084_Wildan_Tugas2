#menampilkan informasi program
print("Menghitung Luas Persegi Panjang")

#input nilai panjang dan lebar
pjg =float(input("Masukkan Panjang Persegi Panjang : "))
lbr =float(input("Masukkan Lebar Persegi Panjang :"))

#proses kalkulasi
luas_pp =pjg*lbr

#menampilkan hasil kalkulasi ke layar
print("Luas Persegi Panjang : ", luas_pp)

print("---------------------------------------")

#menampilkan informasi program
print("Menghitung Luas Lingkaran")

#input nilai jari-jari lingkaran
r = float(input("Masukkan jari-jari lingkaran : "))

#proses kalkulasi
luas_lingkaran = (22/7)*(r**2)

#menampilkan hasil kalkulasi ke layar
print("Luas Lingkaran : ", luas_lingkaran)

print("---------------------------------------")

#menampilkan informasi program
print("Menghitung Luas Permukaan Kubus")

#input nilai panjang sisi kubus
s = float(input("Masukkan panjang sisi kubus : "))

#proses kalkulasi
luas_kubus = 6*(s**2)

#menampilkan hasil kalkulasi ke layar
print("Luas Permukaan Kubus : ", luas_kubus)

print("--------------------------------------- ")

#menampilkan informasi program
print("Konversi suhu dari Celcius ke Fahrenheit")

#input suhu dalam Celcius
C = float(input("Masukkan suhu dalam Celcius : "))

#proses kalkulasi
F = (9/5*C) + 32

#menampilkan hasil kalkulasi ke layar
print("Suhu dalam Celcius : ", C)
print("Suhu dalam Fahrenheit : ", F)

print("--------------------------------------- ")

#menampilkan informasi program
print("Konversi suhu dari Reamur ke Kelvin")

#input suhu dalam Reamur
R = float(input("Masukkan suhu dalam Reamur : "))

#proses kalkulasi
K = (5/4*R) + 273

#menampilkan hasil kalkulasi ke layar
print("Suhu dalam Reamur : ", R)
print("Suhu dalam Kelvin : ", K)

