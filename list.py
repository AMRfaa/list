# inisiasi List
buah_buahan = ["naga","rambutan", "mangga", "jambu"]
panjang_my_list = len(buah_buahan)

# cetak List
print("buah-buahan: ", buah_buahan)
print("panjang list: ", panjang_my_list)
print("panggil index ke 3: ", buah_buahan[3])

# Tmabah anggota di dalam List
buah_buahan.append("pisang")

# Cetak List setelah input anggota baru
print("buah_buahan setelah diinput nilai baru", buah_buahan)

# menghapus nilai mangga di dalam list
buah_buahan.remove("mangga")

# Cetak list setelah menghapus nilai 2 yang pertama
print("buah-buahan setelah menghapus nilai mangga: ", buah_buahan)

#menghapus index ke 1
del buah_buahan[1]

# Cetak list setelah menghapus index ke 1
print("buah_buahan setelah menghapus index ke 1: ", buah_buahan)
