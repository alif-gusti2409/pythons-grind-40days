print("=== perpuetakaan mini ===")

buku = []

while True:
    print("\n1. tambah buku 2. lihat buku 3. cari buku  4. hapus buku 5. keluar")
    pilihan = input("pilih menu> ")

    if pilihan == "1":
        judul = input("judul buku: ")
        pengarang = input("pengarang: ")
        tahun = input("tahun terbit: ")
        buku.append({"judul": judul, "pengarang": pengarang, "tahun": tahun})
        with open("buku.csv", "a") as f:
            f.write(f"{judul},{pengarang},{tahun}\n")
    elif pilihan == "2":
        for b in buku:
            print(f"{b['judul']} oleh {b['pengarang']} ({b['tahun']})")
    elif pilihan == "3":
        cari_judul = input("judul buku yang dicari: ")
        hasil = [b for b in buku if cari_judul.lower() in b['judul'].lower()]
        for b in hasil:
            print(f"{b['judul']} oleh {b['pengarang']} ({b['tahun']})")
    elif pilihan == "4":
        hapus_judul = input("judul buku yang dihapus: ")
        buku = [b for b in buku if b['judul'] != hapus_judul]
    elif pilihan == "5":
        break