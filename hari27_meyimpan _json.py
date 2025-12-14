import json

# Data awal
data = [
    {"nama": "alif", "nilai": 90},
    {"nama": "budi", "nilai": 85},
]

# Simpan data awal
with open("data.json", "w") as f:
    json.dump(data, f)

# Baca data
with open("data.json", "r") as f:
    hasil = json.load(f)
    print(hasil)

# Tanya lanjut
while True:
    lanjut = input("lanjutkan? (y/n): ")
    if lanjut.lower() == "y":
        break
    elif lanjut.lower() == "n":
        exit()
    else:
        print("pilihan tidak valid, masukkan y atau n")

# Menu CRUD
print("crud dengan json")
print("1. create, 2. read, 3. update, 4. delete, 5. simpan")

while True:
    pilihan = input("masukkan pilihan (1/2/3/4/5): ")
    if pilihan in ["1", "2", "3", "4", "5"]:
        break
    else:
        print("pilihan tidak valid, masukkan 1,2,3,4 atau 5")

# CREATE
if pilihan == "1":
    nama_baru = input("masukkan nama baru: ")
    nilai_baru = int(input("masukkan nilai baru: "))
    data.append({"nama": nama_baru, "nilai": nilai_baru})
    with open("data.json", "w") as f:
        json.dump(data, f)
    print("data berhasil ditambahkan")

# READ
elif pilihan == "2":
    read_nama = input("masukkan nama yang akan dibaca: ")
    ditemukan = False
    for item in data:
        if item["nama"] == read_nama:
            print(f"nama: {item['nama']}, nilai: {item['nilai']}")
            ditemukan = True
            break
    if not ditemukan:
        print("nama tidak ditemukan")

# UPDATE
elif pilihan == "3":
    nama_update = input("masukkan nama yang akan diupdate: ")
    ditemukan = False
    for item in data:
        if item["nama"] == nama_update:
            nilai_baru = int(input("masukkan nilai baru: "))
            item["nilai"] = nilai_baru
            with open("data.json", "w") as f:
                json.dump(data, f)
            print("data berhasil diupdate")
            ditemukan = True
            break
    if not ditemukan:
        print("nama tidak ditemukan")

# DELETE
elif pilihan == "4":
    nama_hapus = input("masukkan nama yang akan dihapus: ")
    ditemukan = False
    for item in data:
        if item["nama"] == nama_hapus:
            data.remove(item)
            with open("data.json", "w") as f:
                json.dump(data, f)
            print("data berhasil dihapus")
            ditemukan = True
            break
    if not ditemukan:
        print("nama tidak ditemukan")

# SIMPAN (READ FILE)
elif pilihan == "5":
    with open("data.json", "r") as f:
        hasil = json.load(f)
    print(hasil)
    print("data berhasil disimpan")
