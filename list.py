buah_buahan = ["naga","rambutan", "mangga", "jambu"]
panjang_buah_buahan = len(buah_buahan)

print("buah-buahan: ", buah_buahan)
print("panjang list: ", panjang_buah_buahan)
print("panggil index ke 3: ", buah_buahan[3])

buah_buahan.append("pisang")
print("buah_buahan setelah diinput nilai baru", buah_buahan)

buah_buahan.remove("mangga")
print("buah-buahan setelah menghapus nilai mangga: ", buah_buahan)

del buah_buahan[1]
print("buah_buahan setelah menghapus index ke 1: ", buah_buahan)
