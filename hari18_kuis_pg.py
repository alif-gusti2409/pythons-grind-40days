print("=== kuis pilihan ganda ===")

soal = [
    {"pertanyaan": "bahas pyhthhon dibuat oleh siapa?","pg":"a.Guido van Rossum, b.Linus Torvalds, c.James Gosling","jawaban":"a"},
    {"pertanyaan": "operator untuk pangkat di python adalah?","pg":"a. **, b. ^, c. %","jawaban":"a"},
    {"pertanyaan": "tipe data untuk teks di python adalah?","pg":"a. int, b. str, c. float","jawaban":"b"},
]
skor = 0
for s in soal:
    print("\n"+s["pertanyaan"])
    print(s["pg"])
    jawaban = input("Jawaban Anda: ")
    if jawaban.lower() == s["jawaban"].lower():
        print("Benar!")
        skor += 10
    else:
        print("Salah!")
print(f"\nskor kamu adalah: {skor}")
