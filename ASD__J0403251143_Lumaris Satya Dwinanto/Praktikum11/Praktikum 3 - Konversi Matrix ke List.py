# =================================
#Nama: Lumaris Satya Dwinanto
#Nim: J0403251143
# Praktikum 3: Adjacency Matrix
# ==================================
matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

def convert_to_list(matrix):
    adj_list = {}
    
    for i in range(len(matrix)):
        # Membuat list kosong untuk setiap node (0, 1, 2, 3)
        adj_list[i] = []
        for j in range(len(matrix[i])):
            # Jika bernilai 1, maka node j adalah tetangga dari node i
            if matrix[i][j] == 1:
                adj_list[i].append(j)
    
    return adj_list

# Menjalankan konversi
hasil_list = convert_to_list(matrix)

# Menampilkan output
print("Hasil Konversi Adjacency Matrix ke Adjacency List:")
for node, neighbors in hasil_list.items():
    print(f"{node}: {neighbors}")
    