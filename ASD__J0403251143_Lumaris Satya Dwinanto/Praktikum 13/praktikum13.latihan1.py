# Nama : Lumaris Satya Dwinanto
# NIM : J0403251143
# Kelas : TPL A
# Praktikum 13 - Graph III: Spanning Tree
# ===================================================

# Daftar edge graph
edges = [
('A', 'B'),
('A', 'C'),
('A', 'D'),
('C', 'D'),
('B', 'D')
]
# Contoh spanning tree
spanning_tree = [
('A', 'C'),
('C', 'D'),
('D', 'B')
]
print("Edge pada graph:")
for edge in edges:
    print(edge)
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))


# Jawaban Analisis:
# 1. Graph awal memiliki lebih banyak edge dan masih memungkinkan adanya cycle.
#    Sedangkan spanning tree adalah bagian dari graph yang tetap menghubungkan
#    semua node, tapi tidak memiliki cycle.
#
# 2. Spanning tree tidak boleh memiliki cycle karena cycle membuat edge menjadi
#    berlebih. Jika semua node sudah terhubung, edge tambahan yang membentuk
#    siklus tidak diperlukan dan dapat membuat biaya menjadi lebih besar.
#
# 3. Jumlah edge spanning tree selalu lebih sedikit karena spanning tree hanya
#    membutuhkan edge minimum untuk menghubungkan semua node.
#    Jika jumlah node adalah n, maka jumlah edge pada spanning tree adalah n - 1.