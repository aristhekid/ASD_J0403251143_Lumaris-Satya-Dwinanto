#================================================
# Nama: Lumaris Satya Dwinanto
# Nim: J0403251143
# Kelas: TPL A1
#================================================
def insertionsort(data):
    for indeks in range(1, len(data)):
        key = data[indeks]
        i = indeks
        while i > 0 and data[i-1] > key: #kita tukar tanda yg sebelumnya > menjadi < untuk mengurutkan dari besar ke kecil (descending)
            data[i] = data[i-1]
        data[i] = key
        
data = [59,43,71,15,92,51]
insertionsort(data)
print("Data setelah diurutkan: ", data)