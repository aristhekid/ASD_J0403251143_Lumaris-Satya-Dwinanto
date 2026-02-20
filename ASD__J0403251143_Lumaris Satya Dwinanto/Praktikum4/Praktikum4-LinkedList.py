#=====================================================================
#Nama  : Lumaris Satya Dwinanto
#NIM   : J0403251143
#Kelas : TPL A
#=====================================================================

#=====================================================================
#Implementasi Dasar : Node pada Linked List
#=====================================================================

class Node:
    #konstruktor yabg dijalankan secara otomatis ketika class Node dipanggil/diinstantiasi
    def __init__(self, data):
        self.data = data #meyimpan nilai atau data pada list
        self.data = None #pointer ini menunjuk ke note berikutnya (awal=none)
        
#1.) membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("A")
nodeC = Node("C")

#2.) Menghubungkan Node : A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#3.) Travesal : Menelusuri node dari head sampai ke None
current = head
while current is not None:
    print(current) #Menampilkan data pada node seperti ini
    currtent = current.next #pindah ke node berikutnya
    
 
        
