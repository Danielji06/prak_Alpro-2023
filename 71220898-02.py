dadu_1 = int(input("Masukkan nilai dadu 1: "))
dadu_2 = int(input("Masukkan niali dadu 2: "))
dadu_3 = int(input("Masukkan nilai dadu 3: "))

if (dadu_1 + dadu_2 + dadu_3) == 18:
    hasil = "Royal"
elif dadu_1 == dadu_2 and dadu_2 == dadu_3:
    hasil = "Triple"
elif dadu_1 == 4 and dadu_2 == 5 and dadu_3 == 6:
    hasil = "Flush"
elif dadu_1 == dadu_2 or dadu_2 == dadu_3 or dadu_1 == dadu_3:
    hasil = "Double"
else:
    hasil = "single"

print(f"dadu1={dadu_1}, dadu2={dadu_2}, dadu3={dadu_3}. Maka hasilnya adalah {hasil}")