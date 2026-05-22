# ==========================================================
# Nama : Lumaris Satya Dwinanto
# NIM : J0403251143
# Kelas : TPL A
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================
# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================
import heapq
# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    priority_queue = [(0, start)]
 
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances
hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")
    
# Jawaban Analisis:
# 1. Lokasi yang paling dekat dari Gerbang adalah Kantin,
#    karena jarak terpendek dari Gerbang ke Kantin adalah 2 menit.
#
# 2. Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit.
#    Jalur terbaiknya adalah Gerbang -> Kantin -> Lab -> Aula.
#    Total waktunya adalah 2 + 4 + 1 = 7 menit.
#
# 3. Jalur langsung tidak selalu menghasilkan jarak paling kecil.
#    Dalam weighted graph, yang menentukan jalur terbaik adalah total bobot,
#    bukan hanya apakah jalurnya langsung atau tidak. Bisa saja jalur yang
#    melewati beberapa lokasi memiliki total waktu lebih kecil dibandingkan
#    jalur yang terlihat lebih langsung.
#
# 4. Dijkstra cocok digunakan pada kasus lokasi kampus ini karena semua bobot
#    berupa waktu tempuh bernilai positif. Selain itu, tujuan dari kasus ini
#    adalah mencari waktu tempuh paling kecil dari Gerbang ke lokasi lainnya,
#    sehingga sesuai dengan konsep shortest path pada Dijkstra.
