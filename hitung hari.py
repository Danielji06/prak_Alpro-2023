def hitung_hari(sekarang, n):
    nama_hari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]
    no_hari = nama_hari.index(sekarang)
    n = n % 7
    hasil = (no_hari + n) % 7
    print(nama_hari[hasil])