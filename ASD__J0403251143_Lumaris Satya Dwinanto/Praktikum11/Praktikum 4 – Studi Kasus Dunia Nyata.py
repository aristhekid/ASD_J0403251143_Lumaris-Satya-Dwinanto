#=========================================
#Nama: Lumaris Satya Dwinanto
#Nim: J0403251143
# Praktikum 4 - Studi Kasus Dunia Nyata
# Topik: Jaringan Komputer
#============================================


# 1. Menentukan Node (Vertex) -> Perangkat Jaringan
nodes = ["Router_A", "Router_B", "Switch_1", "Server_1", "PC_1"]

# 2. Menentukan Hubungan Antar Node (Edge) -> Kabel/Koneksi
edges = [
    ("Router_A", "Router_B"),  # Koneksi antar router
    ("Router_A", "Switch_1"),  # Router A ke Switch
    ("Router_B", "Switch_1"),  # Router B ke Switch (Redundansi)
    ("Switch_1", "Server_1"),  # Switch ke Server
    ("Switch_1", "PC_1"),      # Switch ke PC
    ("Router_B", "Server_1")   # Jalur khusus / direct link Router B ke Server
]

print("--- OUTPUT PROGRAM STUDI KASUS JARINGAN KOMPUTER ---")
print("Nama Node (Vertex):", nodes)
print("Hubungan Antar Node (Edge):", edges)
print("-" * 50)

# 3. Implementasi Adjacency List
# Inisialisasi dictionary kosong untuk setiap node
adj_list = {node: [] for node in nodes}

for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u) # Undirected graph (komunikasi dua arah)

print("\n1. Adjacency List:")
for node, neighbors in adj_list.items():
    print(f"{node}:", end=" ")
    for neighbor in neighbors:
        print(neighbor, end=" ")
    print()

# 4. Implementasi Adjacency Matrix
V = len(nodes)
adj_matrix = [[0 for _ in range(V)] for _ in range(V)]

# Bikin bantuan dictionary untuk tau index setiap node (0, 1, 2, dst)
node_idx = {node: i for i, node in enumerate(nodes)}

for u, v in edges:
    idx_u = node_idx[u]
    idx_v = node_idx[v]
    adj_matrix[idx_u][idx_v] = 1
    adj_matrix[idx_v][idx_u] = 1 # Undirected graph

print("\n2. Adjacency Matrix:")
for row in adj_matrix:
    for val in row:
        print(val, end=" ")
    print()
    