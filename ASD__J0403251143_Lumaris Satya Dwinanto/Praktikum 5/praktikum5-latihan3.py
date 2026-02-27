#================================================
# Nama: Lumaris Satya Dwinanto
# Nim: J0403251143
# Kelas: TPL A1
#================================================

#================================================
#Latihan 3 - Mencari nilai Maksimum dalam list
#================================================

def cari_maks(data, index=0):
    # Base case: Jika index udah ada di elemen paling akhir dari list,
    # maka kembalikan nilai elemen tersebut.
    if index ==len(data) - 1:
        return data[index]

# Recursive case: mencari nilai maks dari sisa list disebelah kanannya.
    maks_sisa = cari_maks(data, index + 1)
    
    # membandingkan elemen saat ini dengan nilai maksimum dari elemen sisa.
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa
    
# Contoh penggunaan
angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka)) # Outputnya: 9

#Alur Program:
# Fungsi ini bekerja dengan cara membagi masalah menjadi bagian bagian yang lebih kecil
# Alih alih membangdingkan semuanya sekaligus, fungsi ini membandingkan 1 elemen di index saat ini, dengan
   # "nilai maksimum dari sisa array di kanannya" (didapat dari rekursi maks_sisa).
# Proses memanggil diri sendiri (winding) akan terus maju sampai elemen terakhir list (index 4 nilainya 5). Setelah itu, ia akan mundur
 # (unwinding) sambil membawakan nilai terbesar yang ditemukan sejauh ini untuk dibandingkan dengan elemen sebelumnya (9 vs 5, 2 vs 9, 7 vs 9, 3 vs 9)
 # sampai ditemukan nilai maksimum absolut (9).
 
    
