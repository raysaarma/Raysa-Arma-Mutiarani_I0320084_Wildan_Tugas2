#Menampilkan informasi Program
print('\033[1m' + "IDENTITAS PRIBADI" + '\033[0m')

#Input Identitas Pribadi
namaD = "Raysa Arma"
namaB = "Mutiarani"
nama = namaD + namaB
agama = "Islam"
jk = "Perempuan"
alamat_jalan = "Jalan Kayu Tangan IV"
alamat_no = int(19)
alamt_kodepos = int(59415)
alamat_kab = "Jepara, Jawa Tengah"
hobi = "Menonton dan Memasak"
tb = float(169.7)
uk = float(41.0)
jurusan = "S-1 Teknik Industri"
angkatan = int(2020)
ptn = "Universitas Sebelas Maret"

#Menampilkan data ke layar
print("Nama : ",nama, "\n", "Agama : ", agama, "\n", "Jenis Kelamin : ", jk)
print("-----------------------------------")
print("Alamat : ", alamat_jalan,"No.", alamat_no,"\n", alamat_kab, alamt_kodepos)
print("-----------------------------------")
print("Hobi : ", hobi)
print("Tinggi Badan : ", tb)
print("Ukuran kaki : ", uk)
print("-----------------------------------")
print("Pendidikan : ", "\n", "Prodi :", jurusan, "\n", "Angkatan : ", angkatan, "\n", "Universitas : ", ptn)
print("-----------------------------------")
print("Detail Umur")
#tanggal sekarang
ts = int(input("Tanggal sekarang: "))
bs = int(input("Bulan sekarang: "))
ths = int(input("Tahun sekarang: "))
#tanggal lahir
tl = int(input("Tanggal lahir: "))
bl = int(input("Bulan lahir: "))
thl = int(input("Tahun lahir: "))
#Konversi ke dalam satuan hari
skg = int(ts+(bs*30)+(ths*365))
lhr = int(tl+(bl*30)+(thl*365))
#perhitungan umur
thn = int((skg-lhr)/365)
bln = int(((skg-lhr)%365)/30)
hr = int(((skg-lhr)%365)%30)
print(thn, "Tahun", bln, "Bulan", hr, "Hari")



