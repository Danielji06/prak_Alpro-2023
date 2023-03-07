import random

def generate_angka_komputer(batas):
    hasil = random.randrange(0, batas+1)
    return hasil

def game(angka_komputer):
    print("=== Program Tebak ===")
    menang = False
    while menang == False:
        tebakan = int(input("masukkan tebakan anda: "))
        if tebakan == angka_komputer:
            print("Tebakan anda benar. Anda menang!")
            menang = True
        else:
            print("Tebakan anda salah! Silahkan coba lagi")
            if tebakan > angka_komputer:
                print("Tebakan anda terlalu besar")
            else:
                print("Tebakan anda terlalu kecil")
#program utama
#1. generate angka random
angka_komputer = generate_angka_komputer(100)
game(angka_komputer)