#Inisiasi List
my_list = ["prodi TI", 1,2,3,4,1,2]

# Mengetahui panjang list
panjang_my_lest = len(my_list)

# Cetak List
print("my_list: ",my_list)
print("panjang list : ,"panjang_my_list)
print("panggil index ke 5: ", my_list[5])

# Tambah anggota dalam list 
my_list.append("keren")

# Cetak list setelah input anggota baru
print("my_list setelah diinput nilai baru: ", my_list) 

# Menghapus nilai 2 di dalam list
my_list.remove(2)

# Cetak list setelah menghapus nilai 2 yang pertama
print("my_list setelah menghapus nilai 2: ", my_list)

# menghapus index ke 1
del my_lis[1]

# Cetak list setelah menghapus index ke 1
print("my_list setelah menghapus index ke 1: ", my_list)
