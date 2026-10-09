#List: Koleksi Serbaguna
nilai = [80, 65, 90]
nilai.append(75)
nilai.remove(65)
nilai[0] = 85

print(nilai)
print(nilai[-1], len(nilai))
print(sorted(nilai))



#Tuple: Data yang Tidak Berubah
titik = (3, 7)
warna = (255, 128, 0)

x, y = titik        # unpacking
print(f"x={x}, y={y}")
print(warna[0], len(warna))

print(titik[0])    # TypeError!



#Set: Kumpulan Nilai Unik
angka = {1, 2, 2, 3, 3, 3}
print(angka)

ipa = {"Ani", "Budi", "Citra"}
ips = {"Budi", "Dodi"}

print(ipa | ips)
print(ipa & ips)
print(ipa - ips)



#Dictionary: Pasangan Key-Value
siswa = {"nama": "Sari", "umur": 19}
siswa["kota"] = "Bandung"
siswa["umur"] = 20
print(siswa["nama"])
print(siswa.get("hobi", "-"))

for k, v in siswa.items():
    print(f"{k}: {v}")