#================================================
# Nama: Lumaris Satya Dwinanto
# Nim: J0403251143
# Kelas: TPL A1
#================================================
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] < alist[i+1]: #kita tukar tanda yg sebelumnya > menjadi < untuk mengurutkan dari besar ke kecil (descending)
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum - 1
        
alist = [20, 10, 15, 30, 25, 5, 40, 35, 50, 45]
shortBubbleSort(alist)
print("Data setelah diurutkan: ", alist)