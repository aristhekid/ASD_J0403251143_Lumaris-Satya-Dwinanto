# ==========================================================
# Nama : Lumaris Satya Dwinanto
# NIM : J0403251143
# Kelas : TPL A
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================
# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================
# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}
def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """
    # Semua jarak awal dibuat tak hingga
    
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances
hasil = bellman_ford(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)
    
# Jawaban Analisis:
# 1. Bobot langsung dari A ke B adalah 5.
#
# 2. Total bobot jalur A -> C -> B adalah 2.
#    Perhitungannya adalah A ke C = 4, lalu C ke B = -2.
#    Jadi totalnya 4 + (-2) = 2.
#
# 3. Jalur yang menghasilkan jarak lebih kecil menuju B adalah A -> C -> B,
#    karena total bobotnya 2. Jalur ini lebih kecil dibandingkan jalur langsung
#    A -> B yang bobotnya 5.
#
# 4. Bellman-Ford dapat digunakan pada graph dengan bobot negatif karena
#    algoritma ini tidak langsung menganggap suatu jarak sebagai hasil final.
#    Bellman-Ford melakukan pengecekan dan pembaruan jarak secara berulang,
#    sehingga jalur dengan bobot negatif masih dapat diperhitungkan dengan benar.
#
# 5. Relaksasi edge adalah proses memeriksa apakah jarak menuju suatu node
#    bisa dibuat lebih kecil melalui edge tertentu. Jika ditemukan jalur yang
#    lebih pendek, maka nilai jaraknya diperbarui.
#
# 6. Perbedaan utama Bellman-Ford dan Dijkstra adalah pada cara kerja dan
#    kemampuannya terhadap bobot negatif. Dijkstra lebih cepat, tetapi tidak
#    cocok untuk bobot negatif. Bellman-Ford lebih lambat, tetapi dapat menangani
#    graph yang memiliki bobot negatif.