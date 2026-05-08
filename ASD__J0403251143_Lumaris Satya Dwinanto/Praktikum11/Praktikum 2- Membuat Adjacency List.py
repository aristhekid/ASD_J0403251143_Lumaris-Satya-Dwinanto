#=========================================
#Nama: Lumaris Satya Dwinanto
#Nim: J0403251143
# Praktikum 2 - Adjacency List
#============================================
def createGraph(nodes, edges):
    # Inisialisasi dictionary secara manual
    adj = {node: [] for node in nodes}
    
    # Tambahkan setiap edge ke adjacency list
    for it in edges:
        u = it[0]
        v = it[1]
        adj[u].append(v)
        # Karena graph tidak berarah (undirected), tambahkan sebaliknya
        adj[v].append(u)
        
    return adj

if __name__ == "__main__":
    # Inisialisasi node berupa huruf
    nodes = ['A', 'B', 'C', 'D']
    
    # Daftar sisi/edge (u, v) sesuai gambar: A-B, A-C, B-D, C-D
    edges = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['C', 'D']]
    
    # Bangun graph menggunakan daftar edge
    adj = createGraph(nodes, edges)
    
    print("Adjacency List Representation:")
    for i in nodes:
        # Cetak node/vertex-nya
        print(f"{i}:", end=" ")
        
        for j in adj[i]:
            # Cetak tetangganya (adjacent)
            print(j, end=" ")
        print()