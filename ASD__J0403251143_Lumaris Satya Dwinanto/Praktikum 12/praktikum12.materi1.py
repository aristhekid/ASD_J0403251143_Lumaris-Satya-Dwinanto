# ==========================================================
# Nama : Lumaris Satya Dwinanto
# NIM : J0403251143
# Kelas : TPL A
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================
# ==========================================================
# Materi 1: (Dijkstra)
# ==========================================================
import heapq
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}
def dijkstra(graph, start):
    # Menyimpan jarak minimum
    distances = {node: float('inf') for node in graph}
 
    # Jarak node awal = 0
    distances[start] = 0
 
    # Priority queue
    pq = [(0, start)]
    while pq:
        current_distance, current_node = heapq.heappop(pq)
 
        # Periksa semua tetangga
        for neighbor, weight in graph[current_node].items():
 
            distance = current_distance + weight
 
            # Jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]:
 
                distances[neighbor] = distance
 
                heapq.heappush(pq, (distance, neighbor))
    return distances
hasil = dijkstra(graph, 'A')
print(hasil)

# ==========================================================
# Penjelasan Program:
# Program ini menggunakan algoritma Dijkstra untuk mencari
# jarak terpendek dari satu node ke node lainnya pada
# weighted graph dengan bobot positif.
#
# Graph direpresentasikan menggunakan dictionary bersarang,
# di mana setiap node memiliki tetangga beserta bobotnya.
#
# Algoritma Dijkstra bekerja dengan memilih node yang memiliki
# jarak sementara paling kecil, lalu memperbarui jarak ke
# node-node tetangganya.
#
# Program menggunakan priority queue dari library heapq
# agar proses pemilihan node dengan jarak terkecil menjadi
# lebih efisien.
#
# Pada graph ini:
# A -> B memiliki bobot 4
# A -> C memiliki bobot 2
# B -> D memiliki bobot 5
# C -> D memiliki bobot 1
#
# Hasil akhirnya menunjukkan bahwa jalur tercepat menuju D
# adalah melalui C, karena total bobotnya lebih kecil.
#
# Jalur:
# A -> C -> D = 2 + 1 = 3
#
# Sedangkan:
# A -> B -> D = 4 + 5 = 9
#
# Oleh karena itu jarak terpendek dari A ke D adalah 3.
# ==========================================================