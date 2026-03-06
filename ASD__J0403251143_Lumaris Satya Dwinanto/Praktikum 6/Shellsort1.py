#================================================
# Nama: Lumaris Satya Dwinanto
# Nim: J0403251143
# Kelas: TPL A1
#================================================
def shellsort(data):
    sublistcount = len(data) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(data, startposition, sublistcount)
        
        print("Sublist dengan gap", sublistcount, ":", data)
        sublistcount = sublistcount // 2
        
def gapInsertionSort(data, start, gap):
    for i in range(start + gap, len(data), gap):
        currentvalue = data[i]
        position = i
        
        while position >= gap and data[position - gap] > currentvalue: 
            data[position] = data[position - gap]
            position = position - gap
            
        data[position] = currentvalue
data = [59,43,71,15,92,51, 23, 69, 140, 90, 80, 30]
shellsort(data)
print("Data setelah diurutkan: ", data)