def hitung(berat, tinggi):
    bmi = berat / (tinggi ** 2)
    return bmi

def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Kurus"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Gemuk"
    else:
        return "Obesitas"
    
def saran_bmi(bmi):
    if bmi < 18.5:
        return "Anda disarankan untuk menambah berat badan dengan pola makan sehat."
    elif 18.5 <= bmi < 24.9:
        return "Pertahankan pola makan dan gaya hidup sehat Anda."
    elif 25 <= bmi < 29.9:
        return "Disarankan untuk mengurangi berat badan melalui diet dan olahraga."
    else:
        return "Segera konsultasikan dengan dokter untuk penanganan lebih lanjut."

print("==Kalkulator BMI==")
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))

nilai_bmi = hitung(berat, tinggi)
print(f"Nilai BMI Anda: {nilai_bmi:.2f}")
kategori = kategori_bmi(nilai_bmi)
print(f"Kategori BMI Anda: {kategori}")
saran = saran_bmi(nilai_bmi)
print(f"Saran: {saran}")