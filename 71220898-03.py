p_1 = int(input("Masukkan nilai pemain 1: "))
p_2 = int(input("Masukkan nilai pemail 2: "))
p_3 = int(input("Masukkan nilai pemain 3: "))

if p_1 > 21 and p_2 > 21 and p_3 >21:
    hasil = "maka tidak ada pemenang"
elif p_1 == p_2 == p_3:
    hasil = "maka tidak ada pemenang"
elif  p_1 <= 21 and p_1 > p_2 and p_1 > p_3:
    hasil = "pemenangnya adalah p_1"
elif p_2 <= 21 and p_2 > p_1 and p_2 > p_3:
    hasil = "pemenangnya adalah p_2"
elif p_3 <= 21 and p_3 > p_1 and p_3 > p_2:
    hasil = "pemenangnya adalah p_3"
elif p_1 <= 21 and abs(21 - p_1) < abs(21 - p_2) and abs(21 - p_1) < abs(21 - p_3):
    hasil = "pemenangnya adalah p_1"
elif p_2 <= 21 and abs(21 - p_2) < abs(21 - p_1) and abs(21 - p_2) < abs(21 - P_3):
    hasil = "pemenangnya adalah p_2"
elif p_3 <= 21 and abs(21 - p_3) < abs(21 - p_1) and abs(21 - p_3) < abs(21 - p_2):
    hasil = "pemenangnya adalah p_3"

print(f"p1={p_1}, p2={p_2}, p3={p_3} maka pemenangnya adalah {hasil}")