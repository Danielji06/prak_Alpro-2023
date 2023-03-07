def cek_prima(n): # => True/False
    # prima => hanya habis di bagi 1 dan n => pembaginya cuma ada 2
    pembagi = 0
    for i in range(1, n+1):
        if n % 1 == 0:
            pembagi = pembagi + 1
    if pembagi == 2:
        return True
    else:
        return False 
#program utama
#input user
print("Program pengecekan bilangan prima")
n = int(input("Masukkan bilangan: "))
#proses
hasil = cek_prima(n) # True/False
#output
if hasil == True: #hasilnya True/False
    print(f"{n} adalah bilangan prima")
else:
    print(f"{n} bukan bilangan prima")