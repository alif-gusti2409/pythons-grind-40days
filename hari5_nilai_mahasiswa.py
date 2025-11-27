print("=== hitung nilai akhir semester mahsiswa ===")

tugas = float(input("nailai tugas: "))
uts = float(input("nilai uts: "))
uas = float(input("nilai uas: "))

nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

if nilai_akhir >= 85:
    grade = "A"
elif nilai_akhir >= 75:
    grade = "B"
elif nilai_akhir >= 65:
    grade = "C"
elif nilai_akhir >= 50:
    grade = "D"
else:
     grade = "E"
if nilai_akhir>= 75:
    status = "lulus"
else:
    status = "todak lulus "

print(f"nilai akhir: {nilai_akhir:.2f}")
print(f"grade: {grade}")
print(f"stustus:{status}")