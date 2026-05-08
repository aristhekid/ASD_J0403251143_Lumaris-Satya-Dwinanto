# =================================
#Nama: Lumaris Satya Dwinanto
#Nim: J0403251143
# Praktikum 1: Adjacency Matrix
# ==================================
def createGraph(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]
    
    # Tambahkan setiap edge ke adjacency matrix
    for it in edges:
        u = it[0]
        v = it[1]
        mat[u][v] = 1
        # Karena graph tidak berarah (undirected), tambahkan sebaliknya
        mat[v][u] = 1
        
    return mat

if __name__ == "__main__":
    V = 4
    
    # Daftar sisi/edge (u, v) sesuai gambar: 0-1, 0-2, 1-3, 2-3
    edges = [[0, 1], [0, 2], [1, 3], [2, 3]]
    
    # Bangun graph menggunakan daftar edge
    mat = createGraph(V, edges)
    
    print("Adjacency Matrix Representation:")
    for i in range(V):
        for j in range(V):
            print(mat[i][j], end=" ")
        print()

# Penjelasan arti setiap baris (Wajib dilampirkan):
# Baris 0 (0 1 1 0): Node 0 terhubung dengan Node 1 dan 2.
# Baris 1 (1 0 0 1): Node 1 terhubung dengan Node 0 dan 3.
# Baris 2 (1 0 0 1): Node 2 terhubung dengan Node 0 dan 3.
# Baris 3 (0 1 1 0): Node 3 terhubung dengan Node 1 dan 2.