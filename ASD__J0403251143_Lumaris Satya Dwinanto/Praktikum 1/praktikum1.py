print("============NYOBAAAAAAAA==============")
with open('data_mahasiswa.txt', 'r') as file:
    data = file.readlines()
    
for line in data:
    nama, nim, nilai = line.strip().split(',')
    print(f'Nama: {nama}, NIM: {nim}, nilai: {nilai}')
    
 #=============================================================================
#Praktikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 1 : Membuka file dalam satu string
#=============================================================================   
  
print("============MEMBUKA FILE DALAM SATU STRING==============")
with open("data_mahasiswa.txt", 'r', encoding="utf-8") as file:
    isi_file = file.read()
    print(isi_file)
    
    print("Tipe Data :", type(isi_file))
    
#=============================================================================
#Praktikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 2 : Membuka file per baris
#=============================================================================
    
    print("============MEMBUKA FILE PER BARIS==============")
jumlah_baris = 0 #ini inisialisasi variabel untuk menghitung jumlah baris
with open("data_mahasiswa.txt", 'r', encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #menghilangkan karakter baris baru
        print("Baris ke -", jumlah_baris)
        print("isinya :", baris)
    
    #Parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom2 data
    
with open("data_mahasiswa.txt", 'r', encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(',')
        print ("NIM :", nim, "| Nama :", nama, "| Nilai :", nilai) 
        
#=============================================================================
#Praktikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 3 : Membaca data dan menyimpannya
#=============================================================================



datalist = [] #inisialisasi list kosong untuk menyimpan data mahasiswa
with open("data_mahasiswa.txt", 'r', encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(',') #pecah menjadi data satuan dan simpan ke variabel
        datalist.append([nim, nama,int(nilai)] ) #simpan data ke dalam list
print() 
print("===========Menampilkan data dari list============")
print(datalist)
print("Contoh record ke 1", datalist[0])
print("Contoh nama dari record ke 2", datalist[1])

#=============================================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 4 : Membaca Data dan menyimpannya ke Struktur Data Dictionary
#=============================================================================

data_dict = {} #inisialisasi dictionary kosong untuk menyimpan data 

with open("data_mahasiswa.txt", 'r', encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(',') #pecah menjadi data satuan dan simpan ke variabel
        #simpan data dalam dictionary
        data_dict[nim] = {
            'Nama': nama,
            'Nilai': int(nilai)
                          }
print()
print()

print("===========Menampilkan data dari dictionary============")
print(data_dict)      