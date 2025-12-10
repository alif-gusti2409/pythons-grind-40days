class buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

class perpustakaan:
    def __init__(self):
        self.koleksi = []

    def tambah(self, buku):
        self.koleksi.append(buku)
    
    def tampil(self):
        for b in self.koleksi:
            print(f"{b.judul} - {b.penulis}")

    def cari(self, judul):
        for b in self.koleksi:
            if b.judul.lower() == judul.lower():
                return b
        return None
    
    def hapus(self, judul):
        buku_dihapus = self.cari(judul)
        if buku_dihapus:
            self.koleksi.remove(buku_dihapus)
            return True
        return False

p = perpustakaan()
p.tambah(buku("Laskar Pelangi", "Andrea Hirata"))
p.tambah(buku("Bumi Manusia", "Pramoedya Ananta Toer"))
p.tambah(buku("1984", "George Orwell"))
print("Koleksi Buku di Perpustakaan:")
p.tampil()
judul_cari = input("Masukkan judul buku yang ingin dicari: ")
buku_ditemukan = p.cari(judul_cari)
if buku_ditemukan:
    print(f"Buku ditemukan: {buku_ditemukan.judul} - {buku_ditemukan.penulis}")
else:
    print("Buku tidak ditemukan.")
judul_hapus = input("Masukkan judul buku yang ingin dihapus: ")
if p.hapus(judul_hapus):
    print("Buku berhasil dihapus.")
else:
    print("Buku tidak ditemukan, tidak dapat dihapus.")
print("Koleksi Buku setelah penghapusan:")
p.tampil()
