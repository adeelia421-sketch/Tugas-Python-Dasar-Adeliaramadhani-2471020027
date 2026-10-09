#if_else (Mengambil keputusan)
nilai = 80

if nilai >= 75:
    print("Selamat, kamu lulus!")
else:
    print("Ayo remedial dulu")

print("Program selesai")



#Grade (if-elif-else: Banyak Kondisi)
nilai = 78

if nilai >= 85:
    grade = "A"
elif nilai >= 70:
    grade = "B"
elif nilai >= 55:
    grade = "C"
else:
    grade = "D"

print(f"Nilai {nilai} → grade {grade}")



#Nested if, Ternary &  match-case
#Nested if - if di dalam if
umur, ktp = 20, True
if umur >= 17:
    if ktp:
        print("Boleh memilih")
    else: 
        print("Buat KTP dulu")

#Ternary - if dalam satu baris
umur = 16
s = "dewasa" if umur >= 17 else "anak"
print(s)    # anak

#Match-case - python 3.10+
hari = "sabtu"

match hari: 
    case "sabtu" | "minggu":
        print("Libur!")
    case "senin":
        print("Semangat!")
    case _:
        print("Hari kerja!")