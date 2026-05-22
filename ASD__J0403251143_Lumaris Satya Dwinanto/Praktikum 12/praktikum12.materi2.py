# ==========================================================
# Nama : Lumaris Satya Dwinanto
# NIM : J0403251143
# Kelas : TPL A
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================
# ==========================================================
# Materi 2: (Bellman-Ford)
# ==========================================================
def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
 
    # Relaksasi berulang
    for _ in range(len(graph) - 1):
        
        for node in graph:
 
            for neighbor, weight in graph[node].items():
 
                if distances[node] + weight < distances[neighbor]:
                    
                    distances[neighbor] = distances[node] + weight
    return distances

# ==========================================================
# Penjelasan Program:
# Program ini menggunakan algoritma Bellman-Ford untuk
# mencari jarak terpendek pada weighted graph yang dapat
# memiliki bobot negatif.
#
# Berbeda dengan Dijkstra, Bellman-Ford melakukan proses
# relaksasi edge secara berulang untuk memastikan setiap
# node mendapatkan jarak minimum yang benar.
#
# Graph direpresentasikan menggunakan dictionary bersarang,
# yang menyimpan node tujuan dan bobot edge.
#
# Pada graph ini:
# A -> B memiliki bobot 5
# A -> C memiliki bobot 4
# C -> B memiliki bobot -2
#
# Walaupun jalur langsung dari A ke B memiliki bobot 5,
# ternyata jalur melalui C lebih kecil:
#
# A -> C -> B = 4 + (-2) = 2
#
# Karena terdapat bobot negatif, algoritma Dijkstra tidak
# cocok digunakan pada kasus ini. Oleh sebab itu digunakan
# Bellman-Ford.
#
# Bellman-Ford bekerja dengan memeriksa seluruh edge
# berkali-kali dan memperbarui jarak jika ditemukan
# jalur yang lebih pendek.
#
# Hasil akhirnya menunjukkan bahwa jarak terpendek dari
# A ke B adalah 2 melalui node C.
# ==========================================================