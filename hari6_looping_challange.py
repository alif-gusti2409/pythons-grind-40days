# for loop - pola segitiga
for i in range(1, 6):
    print('*' * i)

# while loop - hitung mundur
print("\nHitung Mundur:")
n = 5
while n > 0:
    print(n)
    n -= 1
print("boom!")

def piramida_terbalik(tinggi):
    # Perulangan luar untuk jumlah baris
    for i in range(tinggi, 0, -1):
        # Perulangan dalam pertama untuk mencetak spasi
        for j in range(tinggi - i):
            print(" ", end="")
        # Perulangan dalam kedua untuk mencetak bintang
        for k in range(2 * i - 1):
            print("*", end="")
        # Pindah baris setelah setiap baris selesai
        print()

# Contoh penggunaan
tinggi_piramida = 5
piramida_terbalik(tinggi_piramida)

#for i in range(tinggi, 0, -1):: Loop ini berjalan dari nilai tinggike 1, membuat jumlah baris menurun.
#for j in range(tinggi - i):: Loop ini mencetak spasi. Jumlah spasi akan berkurang di setiap baris karena isemakin kecil.
#for k in range(2 * i - 1):: Loop ini mencetak bintang. Jumlah bintang berkurang sebanyak 2 di setiap baris karena iberkurang 1.
#print(" ", end="")danprint("*", end="") : Argumen end=""digunakan agar karakter berikutnya dicetak pada baris yang sama, bukan pada baris baru.
#print(): Perintah ini digunakan untuk memindahkan kursor ke baris baru setelah setiap baris pola selesai dicetak . 
