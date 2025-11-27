print("=== konversi detik ke jam, menit, detik ===")
3
total_jam = int(input("{masukkan jumlah jam: }"))
total_menit = int(input("masukkan jumlah menit: "))
total_detik = int(input("masukkan jumlah detik: "))

jam = total_jam*3600
menit = total_menit*60
detik = total_detik

hasil = jam + menit + detik
print(f"hasil: {hasil} detik")

