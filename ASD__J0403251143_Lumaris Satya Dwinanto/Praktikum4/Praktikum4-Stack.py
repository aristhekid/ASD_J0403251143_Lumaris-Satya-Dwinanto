#=====================================================================
#Nama  : Lumaris Satya Dwinanto
#NIM   : J0403251143
#Kelas : TPL A
#=====================================================================

#=====================================================================
#Implementasi Dasar : Stack
#=====================================================================

class Node:
    #konstruktor yabg dijalankan secara otomatis ketika class Node dipanggil/diinstantiasi
    def __init__(self, data):
        self.data = data #meyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)
        
        
        
#Stack ada operasi push(memasukkan head baru) dan pop (menghapus head)

class stack:
    def __init__(self):
        self.top = None #top menunjukkan ke node paling atas (awalnya kosong)
        
    def is_empty(self):
        return self.top is None 
        
    def push(self,data): #memasukkan data baru pada stack
        #1 membuat node baru
        nodeBaru = Node(data) #instantiasi/memanggil konstruktor pada class node
        
        #2 node baru harus menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top
        
        #3 geser head/top lama ke node baru
        self.top = nodeBaru
        
    
    def pop(self): #mengambil/menghapus node paling atas (top/head)
    
        if self.is_empty():
            print("Stack kosong, tidak bisa pop")
            return None    
        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel
        self.top = self.top.next #geser top ke node berikutnya
        return data_terhapus
    
    def peek(self):
        #melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data


    def tampilkan(self):
        current = self.top
        print ("Top ->" , end="  " ) 
        while current is not None:
            print(current.data, end="-> ")
            current = current.next
        print("None")
        
#Instantiasi Class Stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek (Lihat Top): ", s.peek())
s.pop()
s.tampilkan()
print("Peek (Lihat Top): ", s.peek())