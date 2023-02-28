jarak = int(input("Masukkan jarak: "))
batas_a = int(input("Masukkan batas nilai: "))
nilai = int(input("Masukkan nilai: "))

batas_a_minus = batas_a - jarak
batas_b_plus = batas_a_minus - jarak
batas_b = batas_b_plus - jarak
batas_b_minus = batas_b - jarak
batas_c_plus = batas_b_minus - jarak
batas_c = batas_c_plus - jarak
batas_d = batas_c - jarak
batas_e = batas_d - jarak

if nilai >= batas_a:
    hasil = "A" #nilai >= 85
elif nilai >= batas_a_minus:
    hasil = "A-" #nilai >= 80
elif nilai >= batas_b_plus:
    hasil = "B+" #nilai >= 75
elif nilai >= batas_b:
    hasil = "B" #nilai >= 70
elif nilai >= batas_b_minus:
    hasil = "B-" #nilai >= 65
elif nilai >= batas_c_plus:
    hasil = "C+" #nilai >= 60
elif nilai >= batas_c:
    hasil = "C" #nilai >= 55
elif nilai >= batas_d:
    hasil = "D" #nilai >= 50
else:
    hasil = "E" #nilai >= 45

print(f"Jarak={jarak}, batas_a={batas_a}, nilai={nilai}. Maka jawabannya adalah {hasil} ")