# ==========================================================
# Nama : Lumaris Satya Dwinanto
# NIM : J0403251143
# Kelas : TPL A
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================
# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================
import heapq
# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}
def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    
    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue
        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances
hasil = dijkstra(graph, 'A')
        
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban analisis:
# 1. Jarak terpendek dari A ke B adalah 4.
#    Jalurnya langsung dari A ke B dengan bobot 4.
#
# 2. Jarak terpendek dari A ke C adalah 2.
#    Jalurnya langsung dari A ke C dengan bobot 2.
#
# 3. Jarak terpendek dari A ke D adalah 3.
#    Jalurnya adalah A -> C -> D, dengan total bobot 2 + 1 = 3.
#
# 4. Jarak A ke D lebih kecil melalui C karena jalur A -> C -> D
#    memiliki total bobot 3. Sedangkan jika melalui B, jalurnya
#    A -> B -> D memiliki total bobot 4 + 5 = 9.
#    Karena 3 lebih kecil dari 9, maka jalur melalui C lebih optimal.
#
# 5. Fungsi priority_queue dalam algoritma Dijkstra adalah menyimpan node
#    yang akan diproses berdasarkan jarak sementara terkecil.
#    Dengan priority_queue, algoritma selalu memilih node dengan jarak
#    paling kecil terlebih dahulu agar proses pencarian lebih efisien.
#
# 6. Dijkstra tidak cocok untuk graph dengan bobot negatif karena algoritma ini
#    menggunakan pendekatan greedy. Artinya, node dengan jarak terkecil
#    dianggap sudah final. Jika ada bobot negatif, bisa saja jarak yang sudah
#    dianggap final ternyata masih bisa menjadi lebih kecil, sehingga hasilnya
#    bisa tidak akurat.