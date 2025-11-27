print("=== konversi suhu ===")
print("1 celcius ke fahrenheit")
print("2 farenheit ke celcius")
print("3 celcius ke kelvin")
print("4 farenheit ke kelvin ")

pilihan = input("pilih jenis koneversi(1/4): ")

if pilihan == '1':
    c = float(input("masukkan suhu (c): "))
    f = (c* 9/5) + 32
    print(f"hasil: {f:} F")
elif pilihan == '2':
    f = float(input("masukkan suhu (F):"))
    c = (f - 32) * 5/9
    print(f"hasil: {c:} c" )
elif pilihan == '3':
    c =  float(input("masukkan suhu (c):"))
    k = (c + 273,15)
    print(f"hasil: {k:} k")
elif pilihan == '4':
    f = float(input("masukkan suhu (f): "))
    k = (f - 32) * 5/9 + 273,15
    print(f"hasil: {k:} k")
else:
    print("pilihan tidak valid ")