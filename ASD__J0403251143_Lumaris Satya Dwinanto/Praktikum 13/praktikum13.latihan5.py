# Nama : Lumaris Satya Dwinanto
# NIM : J0403251143
# Kelas : TPL A
# Praktikum 13 - Graph III: Spanning Tree
# ===================================================
# Latihan 5 - Jaringan Jalan Antar Kota
# ==========================================================

# Kasus 1: Jaringan Jalan Antar Kota
# Daftar edge: (bobot, kota1, kota2)
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_bobot = 0
connected = set()

# Algoritma Kruskal sederhana
for weight, u, v in edges:
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_bobot += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot minimum =", total_bobot)

# Jawaban Analisis:
# 1. Kasus yang dipilih adalah Kasus 1, yaitu Jaringan Jalan Antar Kota.
#
# 2. Algoritma yang digunakan adalah Kruskal.
#
# 3. Edge yang dipilih dalam MST adalah:
#    Bogor - Depok = 2
#    Depok - Jakarta = 3
#    Depok - Bandung = 4
#
# 4. Total bobot MST adalah 9.
#    Perhitungannya adalah 2 + 3 + 4 = 9.
#
# 5. Edge tertentu tidak dipilih karena bobotnya lebih besar atau dapat
#    membentuk cycle. Contohnya Bogor - Jakarta = 5 tidak dipilih karena
#    Bogor dan Jakarta sudah bisa terhubung melalui Depok. Jakarta - Bandung = 6
#    juga tidak dipilih karena Bandung sudah terhubung melalui Depok.