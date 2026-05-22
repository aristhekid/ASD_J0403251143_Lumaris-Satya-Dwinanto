# ==========================================================
# Nama : Lumaris Satya Dwinanto
# NIM : J0403251143
# Kelas : TPL A
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================
# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================
# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}
# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D'] # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D'] # A -> C -> D
print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")
    
# Jawaban analisis:
# 1. Total bobot jalur A -> B -> D adalah 9.
#    Perhitungannya adalah A ke B = 4, lalu B ke D = 5.
#    Jadi totalnya 4 + 5 = 9.
#
# 2. Total bobot jalur A -> C -> D adalah 3.
#    Perhitungannya adalah A ke C = 2, lalu C ke D = 1.
#    Jadi totalnya 2 + 1 = 3.
#
# 3. Jalur yang dipilih sebagai jalur terpendek adalah A -> C -> D,
#    karena total bobotnya 3, lebih kecil dibandingkan jalur A -> B -> D
#    yang total bobotnya 9.
#
# 4. Jalur terpendek tidak selalu ditentukan dari jumlah edge paling sedikit,
#    karena pada weighted graph yang diitung adalah total bobotnya.
#    Walaupun jumlah edge sama atau lebih banyak, sebuah jalur tetap bisa
#    menjadi jalur terbaik jika total bobotnya lebih kecil.

