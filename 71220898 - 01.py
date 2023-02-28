nilai_x1 = int(input("Masukkan nilai x2 :"))
nilai_y1 = int(input("Masukkan nilai y1 :"))
nilai_x2 = int(input("Masukkan nilai x2 :"))
nilai_y2 = int(input("Masukkan nilai y2 :"))

jarak = ((nilai_x1-nilai_x2)**2 + (nilai_y1-nilai_y2)**2)**0.5
jarak = int(jarak*10)/10

print(f"Titik ({nilai_x1},{nilai_y1}) dan ({nilai_x2},{nilai_y2}) adalah {jarak}")
