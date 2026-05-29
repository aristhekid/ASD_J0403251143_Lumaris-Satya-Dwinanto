# Nama : Lumaris Satya Dwinanto
# NIM : J0403251143
# Kelas : TPL A
# Praktikum 13 - Graph III: Spanning Tree
# ===================================================

import heapq
graph = {
'A': {'B': 4, 'C': 2, 'D': 5},
'B': {'A': 4, 'D': 3},
'C': {'A': 2, 'D': 1},
'D': {'A': 5, 'B': 3, 'C': 1}
}
def prim(graph, start):
    visited = set([start])
    edges = []
    
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
        
    mst = []
    total_weight = 0

    while edges:
        weight, u, v = heapq.heappop(edges)

        if v not in visited:

            visited.add(v)

            mst.append((u, v, weight))
            total_weight += weight

            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)
    
print("Total bobot =", total)

# Jawaban Analisis:
# 1. Node awal yang digunakan adalah A.
#
# 2. Edge yang dipilih pertama kali adalah A - C dengan bobot 2,
#    karena dari node A, edge A-C memiliki bobot paling kecil dibandingkan
#    A-B = 4 dan A-D = 5.
#
# 3. Prim menentukan edge berikutnya dengan melihat edge berbobot paling kecil
#    yang menghubungkan node yang sudah dikunjungi dengan node yang belum
#    dikunjungi. Jadi, setiap langkah Prim memperluas MST dari node yang sudah ada.
#
# 4. Total bobot MST yang dihasilkan adalah 6.
#    Edge yang dipilih yaitu A-C = 2, C-D = 1, dan D-B = 3.
#    Jadi total bobotnya adalah 2 + 1 + 3 = 6.
#
# 5. Perbedaan pendekatan Prim dan Kruskal adalah:
#    Kruskal memilih edge terkecil secara global dari seluruh graph,
#    sedangkan Prim memulai dari satu node awal lalu memilih edge terkecil
#    yang terhubung dengan node yang sudah dikunjungi.