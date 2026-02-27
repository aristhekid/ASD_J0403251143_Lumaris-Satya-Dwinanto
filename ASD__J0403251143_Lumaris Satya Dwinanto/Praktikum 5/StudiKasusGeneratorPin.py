#================================================
# Nama: Lumaris Satya Dwinanto
# Nim: J0403251143
# Kelas: TPL A1
#================================================

#================================================
# Studi Kasus - Generator PIN
#================================================

def buat_pin(panjang, hasil=""):
    # Base case: jika panjang PIN sudah sesuai, cetak hasil
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    
    # Looping pilihan angka
    for angka in ["0", "1", "2"]:
        #PRUNING: Cek apakah angka udah ada di dalam variabel 'hasil'
        # Jika belum ada, baru fungsi memanggil dirinya sendiri (explore)
        if angka not in hasil:
            buat_pin(panjang, hasil + angka)
        
buat_pin(3)

# Bagaimana caranya mencegah angka yang sama muncul berulang?
# Jawab:
#Cara mencegahnya yaitu dengan menggunakan teknik "Pruning" (pemangkasan cabang) di dalam perulangan for. 
#Sebelum program melakukan rekursi (pemanggilan buat_pin), kita tambahkan dulu kondisi seleksi (if angka not in hasil:). 
#Kondisi ini akan mengecek apakah angka tersebut sudah pernah dipakai sebelumnya. Jika sudah dipakai, program akan melewatkannya dan tidak menelusuri cabang tersebut, sehingga PIN dengan angka berulang (seperti 000, 111, 010) tidak akan terbentuk.
