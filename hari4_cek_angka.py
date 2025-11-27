print("=== analisis angka ===")

angka = int(input("maukkan sebuah angka: "))

if angka > 0:
    status = "positif"
elif angka < 0:
    status = "negatif"
    
else:
    status = "nol"

if angka % 2 == 0:
    sifat = "genap"
else:
    sifat = "ganjil"

if angka % 5 == 0:
    hasil= "kelipatan 5"
else:
    hasil= "bukan kelipatan 5"


print(f"angka {angka} adalah {status} dan {sifat} serta {hasil}")