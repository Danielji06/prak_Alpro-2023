# input tiga bilangan
bilangan1 = int(input("Masukkan bilangan pertama"))
bilangan2 = int(input("Masukkan bilangan kedua"))
bilangan3 = int(input("Masukkan bilangan ketiga"))


digit_kanan1 = bilangan1 % 10
digit_kanan2 = bilangan2 % 10
digit_kanan3 = bilangan3 % 10

if digit_kanan1 == digit_kanan2 and digit_kanan2 == digit_kanan3:
    print("Semua digit paling kirinya sama")
else:
    print("Tidak sama semua")