# Nama : Lumaris Satya Dwinanto
# NIM : J0403251143
# Kelas : TPL A
# Praktikum 13 - Graph III: Spanning Tree
# ===================================================
# Latihan 4 - Jaringan Kabel Antar Gedung
# ==========================================================

# Daftar edge: (bobot, gedung1, gedung2)
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# Mengurutkan edge dari bobot paling kecil
edges.sort()

mst = []
total_biaya = 0
connected = set()

# Algoritma Kruskal sederhana
for weight, u, v in edges:
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_biaya += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total biaya minimum =", total_biaya)

# Jawaban Analisis:
# 1. Algoritma yang digunakan adalah Kruskal.
#
# 2. Edge yang dipilih adalah:
#    GedungC - GedungD = 1
#    GedungA - GedungC = 2
#    GedungB - GedungD = 3
#
# 3. Total biaya minimum adalah 6.
#    Perhitungannya adalah 1 + 2 + 3 = 6.
#
# 4. MST cocok digunakan pada kasus ini karena tujuannya adalah
#    menghubungkan semua gedung dengan biaya pemasangan kabel paling minimum
#    tanpa membuat cycle yang menyebabkan biaya tambahan.