def mergesort(data):
    print("Membagi ", data)
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        mergesort(left_half)
        mergesort(right_half)

        i = 0
        j=0 
        k = 0 

        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]: #kita tukar tanda yg sebelumnya < menjadi > untuk mengurutkan dari besar ke kecil (descending)
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j= j + 1
            k=k + 1

        while i < len(left_half):
            data[k] = left_half[i]
            i= i + 1
            k= k + 1

        while j < len(right_half):
            data[k] = right_half[j]
            j= j + 1
            k = k + 1
            
data = [59,43,71,15,92,51, 23, 69, 140, 90, 80, 30, 10, 20, 40, 60, 70, 100]
mergesort(data)
print("Data setelah diurutkan: ", data)