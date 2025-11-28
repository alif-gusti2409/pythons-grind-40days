print("=== Penghitung Huruf ===")

teks = input("Masukkan teks: ").lower()
frekuensi = {}

for huruf in teks:
    if huruf.isalpha():
        frekuensi[huruf] = frekuensi.get(huruf, 0) + 1

for h, j in sorted(frekuensi.items()):
    print(f"{h} muncul sebanyak {j} kali")
    print("-" * 20)
    
terbanyak = max(frekuensi, key=frekuensi.get)
print(f"Huruf yang paling sering muncul adalah '{terbanyak}' sebanyak {frekuensi[terbanyak]} kali")
print("-" * 20)
sedkit = min(frekuensi, key=frekuensi.get)
print(f"Huruf yang paling jarang muncul adalah '{sedkit}' sebanyak {frekuensi[sedkit]} kali")