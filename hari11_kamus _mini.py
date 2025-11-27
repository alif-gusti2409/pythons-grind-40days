print("==kamus mini==")

kamus = {
    "python": "bahasa pemrograman tingkat tinggi yang digunakan untuk pengembangan web, analisis data, kecerdasan buatan, dan banyak lagi.",
    "variabel": "tempat untuk menyimpan data dalam program.",
    "loop": "struktur kontrol yang digunakan untuk mengulangi blok kode selama kondisi tertentu terpenuhi.",
}

while True:
    print("\menu:")
    print("1. Cari arti kata")
    print("2. Tambah kata baru")
    print("3. hapus kata")
    print("4. tamoilkan semua kata")
    print("5. ubah arti kata")
    print("6. simpan to file")
    print("7. keluar")

    pilih = input("pilih opsi (1-7): ")

    if pilih == '1':
        kata = input("masukkan kata: ").lower()
        arti = kamus.get(kata, "kata tidak ditemuka.")
        print("arti:", arti)
    elif pilih == '2':
        kata_baru = input("masukkan kata baru: ").lower()
        arti_baru = input("masukkan arti kata: ")
        kamus[kata_baru] = arti_baru
        print(f"kata '{kata_baru}' telah ditambahkan.")
    elif pilih == '3':
        kata_hapus = input("masukkan kata yang akan dihapus: ").lower()
        if kata_hapus in kamus:
            kamus.pop(kata_hapus, None)
        print("kata telah dihapus.(jika ada)")
    elif pilih == '4':
        for k,v in kamus.items():
            print(f"{k}: {v}")
    elif pilih == '5':
        kata_ubah = input("masukkan kata yang akan diubah: ").lower()
        if kata_ubah in kamus:
            arti_baru = input("masukkan arti baru: ")
            kamus[kata_ubah] = arti_baru
            print(f"arti kata '{kata_ubah}' telah diubah.")
        else:
            print("kata tidak ditemukan.")
    elif pilih == '6':
        with open("kamus_mini.txt", "w") as file:
            for k, v in kamus.items():
                file.write(f"{k}: {v}\n")
    elif pilih == '7':
        break
    else:
        print("pilihan tidak valid. silakan coba lagi.")

        