class mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        return f"Nama: {self.nama}, NIM: {self.nim}, Jurusan: {self.jurusan}"
mhs1 = mahasiswa("Andi", "123456", "Informatika")
print(mhs1.tampilkan_info())
