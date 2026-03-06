#================================================
# Nama: Lumaris Satya Dwinanto
# Nim: J0403251143
# Kelas: TPL A1
#================================================
def selectionsort(data):
    for angka in range(len(data)-1, 0, -1):
        max_index = 0
        for i in range(1, angka+1):
            if data[i] > data[max_index]:
                max_index = i
        # Tukar data dengan variabel angka dengan data variabel max_index
        temp = data[angka]
        data[angka] = data[max_index]
        data[max_index] = temp
        
data = [15, 23, 92, 140, 51, 69]
selectionsort(data)
print("Data setelah diurutkan: ", data)