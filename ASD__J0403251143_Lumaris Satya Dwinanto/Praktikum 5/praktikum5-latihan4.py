#================================================
# Nama: Lumaris Satya Dwinanto
# Nim: J0403251143
# Kelas: TPL A1
#================================================

#================================================
#Latihan 4 - Kombinasi Huruf
#================================================

def kombinasi(n, hasil=""):
    # Base case: Jika panjang string (hasil) sudah sama dengan batas n, cetak dan berhenti
   
    if len(hasil) == n:
        print(hasil)
        return
    # choose + explore cabang dari 'A'
    kombinasi(n, hasil + "A") # Tambahkan 'A' dan lanjutkan rekursi
    # choose + explore cabang dari 'B'
    kombinasi(n, hasil + "B") # Tambahkan 'B' dan lanjutkan rekursi
    
kombinasi(2) 
#Alur Program:
#Bagaimana jumlah kombinasi yang dihasilkan?
#Jumlah kombinasi yang dihasilkan mengikuti rumus 2^n, di mana n itu panjang string yang diinginkan. Dalam kasus kombinasi(2), akan ada 2^2 = 4 kombinasi yang dihasilkan (AA, AB, BA, BB).
#Hal ini terjadi karena di setiap tingkatan fungsi, program selalu membentuk 2 cabang keputusan (memilih "A" atau memilih "B"). Struktur pemanggilannya membentuk pohon keputusan (decision tree) biner.