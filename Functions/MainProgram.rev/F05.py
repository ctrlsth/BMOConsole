# F05 - Mengubah Game pada Toko Game
import rCSV as r

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
        if A == game_data[i][0]:
            found = True
            index = i

    # Jika ditemukan, merubah data
    if found == True:
        if B != "":
            r.modif(game_data, index, 1, B)
        if C != "":
            r.modif(game_data, index, 2, C)
        if D != "":
            r.modif(game_data, index, 3, int(D))
        if E != "":
            E = r.discard(E, ".")
            r.modif(game_data, index, 4, int(E))
        
        print("Perubahan data game sukses!")

    # Jika tidak, menampilkan pesan error
    else:
        print("ID game tidak ditemukan")

    return

# test case
# import DummyLoad as l

# # Insialisasi
# headergame = []
# datagame = []
# l.game(headergame, datagame)

# headerhis = []
# datahis = []
# l.riwayat(headerhis, datahis)

# headerkep = []
# datakep = []
# l.kepemilikan(headerkep, datakep)

# headeruser = []
# datauser = []
# l.user(headeruser, datauser)

# loginData = [2, "hanhan","Hans", "snah", "user", 20000]

# # manggil fungsi
# for i in datagame:
#     print(i)
# modGameStore(datagame)
# for i in datagame:
#     print(i)
