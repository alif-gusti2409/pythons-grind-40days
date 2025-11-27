import csv
print("to-do list")
todo_list = []

while True:
    print("\nmenu: [1] tambah [2] lihat [3] hapus [4] edit [5] keluar")
    pilih = input("pilih opsi (1-5): ")

    if pilih == '1':
        tugas = input("masukkan tugas baru: ")
        todo_list.append(tugas)
        print(f"tugas '{tugas}' telah ditambahkan.")
    elif pilih == '2':
        for i, t in enumerate(todo_list, start=1):
            print(f"{i}. {t}")
    elif pilih == '3':
        hapus = int(input("masukkan nomor tugas yang akan dihapus: "))
        if 1 <=hapus < len(todo_list):
            todo_list.pop(hapus)
            print("tugas telah dihapus.")
    elif pilih == '4':
        edit = int(input("masukkan nomor tugas yang akan diubah: "))
        if 1 <= edit <= len(todo_list):
            tugas_baru = input("masukkan tugas baru: ")
            todo_list[edit - 1] = tugas_baru
            print("tugas telah diperbarui.")
    elif pilih == '5':
        break
    else:
        print("pilihan tidak valid. silakan coba lagi.")

with open('hari15_todo_list.csv','w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["to-do list"]) 
        for tugas in todo_list:
            writer.writerow([tugas])