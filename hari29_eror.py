try:
    angka = int(input("masukkan angka:"))
    if angka < 0 or angka < 100:
        print(f"angka valid {angka}")
    else:
        print(f"angka tidak valid {angka}")
    hasil =  angka
    print("hasil:", hasil)
except ValueError:
    print("input harus berupa angka bulat!")
except ZeroDivisionError:
    print("tidak bisa membagi dengan nol!")
finally:
    print("terima kasih telah menggunakan program ini.")