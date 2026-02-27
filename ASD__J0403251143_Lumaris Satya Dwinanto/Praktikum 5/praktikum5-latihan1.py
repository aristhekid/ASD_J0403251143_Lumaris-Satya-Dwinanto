#================================================
# Nama: Lumaris Satya Dwinanto
# Nim: J0403251143
# Kelas: TPL A1
#================================================

#================================================
#Latihan 1 - Rekursi Pangkat
#================================================

def pangkat(a, n):

    # Base Case : Kondisi untuk menghentikan rekursi
    # Jika pangkat (n) udah mencapai angka 0, maka fungsi mengembalikan nilai 1 (karena a^0 = 1)
    if n == 0:
        return 1
    
    # Recursive Case : Fungsi ini untuk memanggil dirinya sendiri dengan mengurangi nilai n (n-1)
    # nilai 'a' akan terus dikalikan dengan hasil pengembalian fungsi  pangkat (a, n-1) sampai mencapai base case
    return a * pangkat(a, n-1)

print(pangkat(2, 4)) # Output: 16

#Alur Program:
#1. Fungsi pangkat dipanggil dengan a=2 dan n=4
#2. Fase winding (Masuk): karena n belum 0, fungsi akan mereturn 2 * pangkat (2,3)
#3. Hal ini akan berulang terus 2 * pangkat(2,2) -> 2*
#4. Saat n == 0(saat base case tercapai), fungsi akan megembalikan angka 1
#5. Fase unwinding (Keluar): fungsi berjalan mundur untuk meyelesaikan perkaliannya:
  # 1 * 2 * 2 * 2 * 2 = 16.

        