with open("catatan.txt","w") as file:
    file.write("belajar python hari ke-26\n")

with open("catatan.txt","r") as file:
    isi = file.read()
    print(isi)

with open("catatan.txt","a") as file:
    file.write("menambahkan catatan baru\n")
with open("catatan.txt","r") as file:
    isi = file.read()
    print(isi)
    