import json

class Kontak:
    def __init__(self, nama, nomor):
        self.nama = nama
        self.nomor = nomor

class BukuTelpon:
    def __init__(self):
        self.data = []
    
    def tambah(self, kontak):
        self.data.append(vars(kontak))
        self.simpan()
    
    def simpan(self):
        with open("kontak.json","w") as f:
            json.dump(self.data, f, indent=2)

bt = BukuTelpon()
bt.tambah(Kontak("Alice","08123456789"))

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
    nomor_baru = input("masukkan nomor baru: ")
    bt.tambah(Kontak(nama_baru, nomor_baru))
    print("kontak berhasil ditambahkan")
# READ
elif pilihan == "2":
    read_nama = input("masukkan nama yang akan dibaca: ")
    ditemukan = False
    for item in bt.data:
        if item["nama"] == read_nama:
            print(f"nama: {item['nama']}, nomor: {item['nomor']}")
            ditemukan = True
            break
    if not ditemukan:
        print("nama tidak ditemukan")
# UPDATE
elif pilihan == "3":
    nama_update = input("masukkan nama yang akan diupdate: ")
    ditemukan = False
    for item in bt.data:
        if item["nama"] == nama_update:
            nomor_baru = input("masukkan nomor baru: ")
            item["nomor"] = nomor_baru
            bt.simpan()
            print("kontak berhasil diupdate")
            ditemukan = True
            break
    if not ditemukan:
        print("nama tidak ditemukan")
# DELETE
elif pilihan == "4":
    nama_hapus = input("masukkan nama yang akan dihapus: ")
    ditemukan = False
    for item in bt.data:
        if item["nama"] == nama_hapus:
            bt.data.remove(item)
            bt.simpan()
            print("kontak berhasil dihapus")
            ditemukan = True
            break
    if not ditemukan:
        print("nama tidak ditemukan")
# SIMPAN
elif pilihan == "5":
    bt.simpan()
    print("data berhasil disimpan")