#================================================
# Nama: Lumaris Satya Dwinanto
# Nim: J0403251143
# Kelas: TPL A1
#================================================

#================================================
#Latihan 2 - Tracing Rekursi
#================================================

def countdown(n):
    if n == 0:
        print("selesai")
        return
    
    # Fase Stacking (Masuk): dieksekusi sebelum pemanggilan rekursif
    print("Masuk: ", n)
    
    # Pemanggilan rekursif
    countdown(n - 1)
    
    # Fase unwinding (Keluar): dieksekusi setelah pemanggilan rekursif selesai
    print("Keluar: ", n)
    
countdown(5)

#Alur Program:
# Kenapa output 'Keluar' muncul terbalik?
#Jawab:
# Output 'Keluar' muncul terbalik karena prinsip tumpukan (call stack) pada memori komputer yang bersifat LIFO (Last In, First Out). 
# Saat fungsi countdown(n-1) dipanggil, eksekusi kode di bawahnya (yaitu print("Keluar:", n)) akan ditunda (di-pause) dan ditumpuk di dalam memori.
# Setelah base case (n == 0) tercapai dan mencetak "Selesai", barulah tumpukan fungsi tersebut dibongkar dari yang paling terakhir masuk (n=1) hingga yang paling awal (n=5).
# Inilah yang disebut fase unwinding/mengurai.

