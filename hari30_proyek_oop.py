import json

class mahasiswa:
    def __init__(self, nama, nim, niai):
        self.nama = nama
        self.nim = nim
        self.niai = niai

class sistemmahasiswa:
    def __init__(self):
        self.data = self.load()

    def load(self):
        try:
            with open ("mahasiswa.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def simpan(self):
        with open("mahasiswa.json", "w") as f:
            json.dump(self.data, f, indent=2)

    def tambah(self, m):
        self.data.append(vars(m))
        self.simpan()

    def tampilkan(self):
        for d in self.data:
            print(f"Nama: {d['nama']}, NIM: {d['nim']}, Nilai: {d['niai']}")

sm = sistemmahasiswa()
sm.tambah(mahasiswa("Andi", "12345", 85))

while True:
    print("\nmenu")
    print("1. Tambah mahasiswa")
    print("2. Tampilkan mahasiswa")
    print("3. update mahasiswa")
    print("4. hapus mahasiswa")
    print("5. Keluar")
    pilihan = input("pilih menu (1/2/3/4/5): ")
    if pilihan == "1":
        nama = input("masukkan nama: ")
        nim = input("masukkan NIM: ")
        try:
            niai = int(input("masukkan nilai: "))
            m = mahasiswa(nama, nim, niai)
            sm.tambah(m)
            print("mahasiswa berhasil ditambahkan.")
        except ValueError:
            print("nilai harus berupa angka bulat!")
    elif pilihan == "2":
        sm.tampilkan()
    elif pilihan == "3":
        nim = input("masukkan NIM mahasiswa yang akan diupdate: ")
        for d in sm.data:
            if d['nim'] == nim:
                nama_baru = input("masukkan nama baru: ")
                try:
                    niai_baru = int(input("masukkan nilai baru: "))
                    d['nama'] = nama_baru
                    d['niai'] = niai_baru
                    sm.simpan()
                    print("mahasiswa berhasil diupdate.")
                except ValueError:
                    print("nilai harus berupa angka bulat!")
                break
        else:
            print("mahasiswa dengan NIM tersebut tidak ditemukan.")
    elif pilihan == "4":
        nim = input("masukkan NIM mahasiswa yang akan dihapus: ")
        for i, d in enumerate(sm.data):
            if d['nim'] == nim:
                del sm.data[i]
                sm.simpan()
                print("mahasiswa berhasil dihapus.")
                break
        else:
            print("mahasiswa dengan NIM tersebut tidak ditemukan.")
    elif pilihan == "5":
        print("terima kasih telah menggunakan program ini.")
        break
    else:
        print("pilihan tidak valid, silakan coba lagi.")