print("==== penghitung kata ====")

kalimat1= input("masukkan kalimat: ")
kalimat2=input("masukkan kalimat: ")


kata1 = kalimat1.split()
jumlah_kata = len(kata1)
jumlah_huruf = len(kalimat1.replace(" ", ""))

kata2 = kalimat2.split()
jumlah_kata = len(kata2)
jumlah_huruf = len(kalimat2.replace(" ", ""))

kata_terpanjang = max(kalimat1, kalimat2, key=len)
jumlah_huruf = len(kata_terpanjang.replace(" ", ""))
print(f"kata terpanjang: {kata_terpanjang}")
print(f"jumlah huruf (tanpa spasi): {jumlah_huruf}")

rata_rata_kata = (len(kalimat1.replace(" ", "")) + len(kalimat2.replace(" ", ""))) / (len(kata1) + len(kata2))
print(f"rata-rata jumlah huruf per kata: {rata_rata_kata}")