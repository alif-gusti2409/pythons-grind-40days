def is_palindrome(kata):
    kata = kata.replace(" ", "").lower()
    return kata == kata[::-1]

def are_anagrams(kata1, kata2):
    return sorted(kata1.replace(" ", "").lower()) == sorted(kata2.replace(" ", "").lower())

print("=== Palindrome dan Anagram ===")
print("[1] Cek Palindrome","[2] Cek Anagram")

pilihan = input("Pilih opsi (1 atau 2): ")

if pilihan == "1":
    kata = input("Masukkan kata atau kalimat: ")
    print("Palindrome?", is_palindrome(kata))
elif pilihan == "2":
    kata1 = input("Masukkan kata atau kalimat pertama: ")
    kata2 = input("Masukkan kata atau kalimat kedua: ")
    print("Anagram?", are_anagrams(kata1, kata2))
else:
    print("Opsi tidak valid.")
print("Anagram?", are_anagrams(kata1, kata2))