# ==========================================================
# Nama : Lumaris Satya Dwinanto
# NIM : J0403251143
# Kelas : TPL A
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================
# ==========================================================
# Latihan 5. Studi Kasus dengan Program Shortest Path
# Algoritma : 
import heapq

# Weighted graph antar kota
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Jakarta': {'Bandung': 7},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Bandung': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek
    menggunakan algoritma Dijkstra
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak node awal = 0
    distances[start] = 0

    # Priority queue
    priority_queue = [(0, start)]

    while priority_queue:

        # Mengambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak lebih besar dari data terbaru, skip
        if current_distance > distances[current_node]:
            continue

        # Mengecek semua tetangga
        for neighbor, weight in graph[current_node].items():

            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]:
                distances[neighbor] = distance

                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Menjalankan algoritma dari Bogor
hasil = dijkstra(graph, 'Bogor')

print("Jarak terpendek dari Bogor:")

for kota, jarak in hasil.items():
    print("Bogor ->", kota, "=", jarak)

# ==========================================================
# Jawaban Analisis:
#
# 1. Node awal yang digunakan adalah Bogor.
#
# 2. Node yang memiliki jarak paling kecil dari node awal
#    selain Bogor adalah Depok dengan jarak 2.
#
# 3. Node yang memiliki jarak paling besar dari node awal
#    adalah Bandung dengan jarak 8.
#
# 4. Algoritma Dijkstra bekerja dengan memilih node yang
#    memiliki jarak terkecil terlebih dahulu, kemudian
#    memperbarui jarak ke node tetangganya.
#    Proses ini dilakukan terus sampai semua node
#    mendapatkan jarak minimum.
# ==========================================================