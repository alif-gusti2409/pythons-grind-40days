print("=== pengelolaan nilai siswa ===")

data=[]

while True:
    print("\n1. tambanh 2. lihat 3. hapus 4. edit nilai 5. rata-rata 6. keluar")
    p = input("pilih menu> ")

    if p == "1":
        nama = input("nama : ")
        nilai = float(input("nilai : "))
        data.append({"nama": nama, "nilai": nilai})
    elif p == "2":
        for s in data:
            print(f"{s['nama']} : {s['nilai']}")
    elif p == "3":
        hapus = input("nama yang dihapus: ")
        data = [s for s in data if s['nama'] != hapus]
    elif p == "4":
        edit = input("nama yang di edit: ")
        for s in data:
            if s['nama'] == edit:
                new_nilai = float(input("nilai baru: "))
                s['nilai'] = new_nilai
                break
    elif p == "5":
        if data:
            rata_rata = sum(s['nilai'] for s in data) / len(data)
            print(f"Rata-rata nilai: {rata_rata}")
        else:
            print("Data kosong.")
    elif p == "6":
        break