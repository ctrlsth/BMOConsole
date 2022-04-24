# F04 - Menambah Game Ke Toko Game
import rCSV as r

def addgame(datagame, newgamearray):
# { I.S globaldata terdefinisi; F.S. globaldata ditambahkan elemen (data game) baru }
# prosedur : menambahkan game ke datagame

# KAMUS LOKAL
# parameters
    # globaldata : matriks
    # newgamearray : array
# variable
    # new_id : str
    # datalength : int
    # gameid : array

    # Melihat banyak game dalam current list
    datalength = r.length(datagame)
    new_id = "GAME"

    # Menentukan banyak digit yang harus ditambahkan
    if r.length(str(datalength + 1)) > 1:       # Jika lebih dari 1 digit
        if r.length(str(datalength + 1)) > 2:   # Jika lebih dari 2 digit
            new_id += str(datalength + 1)
        else:                                   # Jika 2 digit
            new_id += "0"
            new_id += str(datalength + 1)
    else:                                       # Jika 1 digit
        new_id += "00"
        new_id += str(datalength + 1)

    # Menyambungkan (ID Game dengan Data Game) dengan Datagame (globaldata)
    game_id = [new_id]                          # Memasukkan ID Game Terbaru
    game_id += newgamearray                     # Konso NewGameArray
    datagame += [game_id]                     # Konso data game baru


    print("Selamat! Berhasil menambahkan game", newgamearray[0])

    return

def newGame(datagame):
# { I.S. globaldata terdefinisi; F.S. globaldata terisi data game terbaru berdasarkan masukan admin }
# prosedur : meminta masukan admin kemudian menambahkan game ke dalam list

# KAMUS LOKAl
# parameter
    # globaldata : matriks
# variables
    # A, B, C, D, E : str
    # newgame : array

# ALGORITMA

    # Meminta masukan
    A = input("Masukkan nama game: ")
    B = input("Masukkan kategori: ")
    C = input("Masukkan tahun rilis: ")
    D = input("Masukkan harga: ")
    E = input("Masukkan stok awal: ")

    # Memeriksa kevalidan masukan
    while A == "" or B == "" or C == "" or D == "" or E == "":
        print()
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan di BiNoMO.")
        A = input("Masukkan nama game: ")
        B = input("Masukkan kategori: ")
        C = input("Masukkan tahun rilis: ")
        D = input("Masukkan harga: ")
        E = input("Masukkan stok awal: ")

    # Memasukkan masukan ke dalam array
    D = r.discard(D, ".")
    newgame = [A, B, int(C), int(D), int(E)]

    # Menambahkannya ke dalam datagame global
    addgame(datagame, newgame)

    return


# # test case
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
# newGame(datagame)
# for i in datagame:
#     print(i)
# print()
# newGame(datagame)
# print()
# for i in datagame:
#     print(i)
