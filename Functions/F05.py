# F05 - Mengubah Game pada Toko Game
import rCSV_rev2 as r

def modGameStore(game_data):
# { I.S. game_data terdefinisi; F.S. value game pada game_data berubah }
# procedure : mengubah game pada toko game

# KAMUS LOKAL
# A,B,C,D,E : str
# found : bool
# index : int

# ALGORITMA

    # Meminta masukan admin
    A = input("Masukkan ID game: ")
    B = input("Masukkan nama game: ")
    C = input("Masukkan kategori: ")
    D = input("Masukkan tahun rilis: ")
    E = input("Masukkan harga: ")

    # Mencari Data sesuai dengan GAMEID yang dimasukkan
    found = False
    index = 0
    for i in range (r.length(game_data)):
        if A in game_data[i][0]:
            found = True
            index = i

    # Jika ditemukan, merubah data
    if found == True:
        if B != "":
            r.modif(game_data, index, 1, B)
        if C != "":
            r.modif(game_data, index, 2, C)
        if D != "":
            D = r.discard(D, ".")
            r.modif(game_data, index, 3, int(D))
        if E != "":
            r.modif(game_data, index, 4, int(E))
        
        print("Perubahan data game sukses!")

    # Jika tidak, menampilkan pesan error
    else:
        print("ID game tidak ditemukan")

    return
