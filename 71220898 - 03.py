detik = int(input("masukkan detik : "))
menit = 60
jam  = menit * 60
hari = jam * 24

hasil_hari = detik // hari
sisa_detik_dalam_hari = detik % hari

hasil_jam = sisa_detik_dalam_hari // jam
sisa_detik_dalam_jam = sisa_detik_dalam_hari % jam

hasil_menit = sisa_detik_dalam_jam // menit
sisa_detik_dalam_menit = sisa_detik_dalam_jam % menit

hasil_detik = sisa_detik_dalam_menit

print(f"{detik} detik = {hasil_hari} hari, {hasil_jam} jam, {hasil_menit} menit, {hasil_detik} detik")