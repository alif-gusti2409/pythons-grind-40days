print("=== program daftar belanja ===")
belanja = []
while True:
    barang = input("masukkan nama barang (atau ketik 'selesai'): ")
    if barang.lower()== 'selesai' :
        break
    belanja.append(barang)

print("\n daftar belanja kamu ")
for item in belanja :
    print("_", item)

print(f"total barang: {len(belanja)} ")

while True:
    hapus = input("masukkan nama barang yang ingin dihapus (atau ketik 'selesai'): ")
    if hapus.lower() == 'selesai':
        break
    if hapus in belanja:
        belanja.remove(hapus)
        print(f"{hapus} telah dihapus dari daftar belanja.")
    else:
        print(f"{hapus} tidak ditemukan dalam daftar belanja.")

    with open("daftar_belanja.txt", "w") as file:
        for item in belanja:
            file.write(item + "\n")
            
            print("\ndaftar belanja telah disimpan ke 'daftar_belanja.txt'")