print("=== klkulator sederhana ===")
print("operasi:+ - * / % **" )
angka1 = float(input("masukkan angka pertama: "))
operator = input("pilih operator(+ - * / % **): ")
angka2 = float(input("masukkkan angka kedua: "))

if operator == '+':
    hasil = angka1 + angka2
elif operator == '-':
    hasil = angka1 - angka2
elif operator == '*':
    hasil = angka1 * angka2
elif operator == '/':
    hasil = angka1 / angka2
elif operator== '%':
    hasil = angka1 % angka2
elif operator == '**':
    hasil = angka1**angka2
else:
    hasil = "operator tidak di kenal"
print("hasil: ", hasil)