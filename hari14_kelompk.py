import random

print("=== pegacak  nama kelompok ===")

nama = input("masukkan nama lengkap (pisahkan dengan koma): ")
daftar_nama = [n.strip() for n in nama.split(",") if n.strip()]

jumlah_kelompok = int(input("masukkan jumlah kelompok: "))

random.shuffle(daftar_nama)

for i in range(jumlah_kelompok):
    kelompok = daftar_nama[i::jumlah_kelompok]
    print(f"Kelompok {i + 1}: {', '.join(kelompok)}")

    with open(f"kelompok_{i + 1}.txt", "w") as file:
        file.write(f"Kelompok {i + 1}:\n")
        for member in kelompok:
            file.write(f"- {member}\n")