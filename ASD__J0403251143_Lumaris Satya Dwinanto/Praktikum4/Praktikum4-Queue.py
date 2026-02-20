#=====================================================================
#Nama  : Lumaris Satya Dwinanto
#NIM   : J0403251143
#Kelas : TPL A
#=====================================================================

#=====================================================================
#Implementasi Dasar : Queue
#=====================================================================

class Node:
    #konstruktor adalah fungsi yang dijalankan secara otomatis ketika class node dipanggil / diinstalasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)
        
class queue:
    # buat konstruktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None # Node paling depan
        self.rear = None  # Node paling belakang
    
    def is_empty(self):
        return self.front is None

    # membuat fungsi untuk menambahkan data baru pada bagian paling belakang
    def enqueue(self, data):
        nodeBaru = Node(data)
        
        #Jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        #Jika queue tidak kosong, 
        self.rear.next = nodeBaru #Letakkan data bar pada setelahnya rear
        self.rear = nodeBaru #Jadikan data baru sebagai rear
        
    def dequeue(self):
        #menghapus data dari depan/front
        data_terhapus = self.front.data #Lihat data paling depan
        
        #geser front ke node berikutnya
        self.front = self.front.next
    def tampilkan(self):
        current = self.front
        print("Front ->", end=' ')
        while current is not None:
            print(current.data, end= "-> ")
            current = current.next
        print (" Rear")
        
#Instantiasi class queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()        