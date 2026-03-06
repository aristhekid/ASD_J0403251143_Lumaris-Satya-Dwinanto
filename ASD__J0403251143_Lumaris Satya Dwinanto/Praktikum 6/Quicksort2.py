#================================================
# Nama: Lumaris Satya Dwinanto
# Nim: J0403251143
# Kelas: TPL A1
#================================================
def quicksort(data):
    quicksort_helper(data, 0, len(data)-1)

def quicksort_helper(data, first, last):
    if first < last:
        pivot_index = partition(data, first, last)
        quicksort_helper(data, first, pivot_index-1)
        quicksort_helper(data, pivot_index+1, last)

def partition(data, first, last):
    pivot_value = data[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:

        while left_mark <= right_mark and data[left_mark] >= pivot_value: # rubah tanda < menjadi > untuk mengurutkan dari besar ke kecil (descending)
            left_mark += 1

        while right_mark >= left_mark and data[right_mark] <= pivot_value: # rubah tanda > menjadi < untuk mengurutkan dari besar ke kecil (descending)
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            data[left_mark], data[right_mark] = data[right_mark], data[left_mark]

    data[first], data[right_mark] = data[right_mark], data[first]

    return right_mark


data = [59,43,71,15,92,51,23,69,140,90,80,30,10,20,40,60,70,100]
quicksort(data)
print("Data setelah diurutkan:", data)