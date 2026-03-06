# modifikasi algoritma short bubble Sort untuk Descending
def shortBubbleSortDescending(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            # Tanda diubah menjadi < agar nilai terbesar bergeser ke kiri (depan)
            if alist[i] < alist[i+1]: 
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum - 1

# Data skor tes pelamar kerja
skor = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

# 1. Urutkan data secara menurun
shortBubbleSortDescending(skor)

# Mengambil 5 data pertama (tertinggi)
lima_tertinggi = skor[:5]

print("Seluruh skor terurut (Descending):", skor)
print("1. Skor 5 kandidat tertinggi:", lima_tertinggi)
print("2. Kandidat yang lolos adalah kandidat dengan skor:", lima_tertinggi)
