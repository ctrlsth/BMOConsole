import rCSV as r

def isFilled(array):
# function: Menentukan kondisi array antara terisi dan tidak terisi

# KAMUS LOKAL
# paramters
    # array : array

# ALGORITMA
    if r.length(array) != 0:
        return True
    else:
        return False

def cariGameInventory(user_id, datagame, datakep):
# prosedur: Menampilkan list game dari inventory seorang user berdasarkan hasil pencarian

# KAMUS LOKAL
# parameters
    # user_id : int
    # datagame : matrix
    # datakep : matrix of str
# variables
    # idgame, year : str
    # foundgame, matched : matrix

# ALGORITMA
    idgame = input("Masukkan ID Game: ")
    idgame = idgame.upper()
    year = input("Masukkan Tahun Rilis Game: ")

    foundgame = []
    for line in datakep:
        if line[1] == user_id:
            for i in datagame:
                if i[0] == line[0]:
                    foundgame += [i]
                    break

    print()
    if isFilled(idgame):

        matched = []
        for game in foundgame:
            if game[0] == idgame:
                matched += [game]

        if isFilled(matched):
            if isFilled(year):
                year = int(year)
                print("Daftar game pada inventory yang memenuhi kriteria:")
                if year == matched[0][3]:
                    r.neatList(matched, False)
                else:
                    print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
            else:
                print("Daftar game pada inventory yang memenuhi kriteria:")
                r.neatList(matched, False)
        else:
            print("Daftar game pada inventory yang memenuhi kriteria:")
            print("Tidak ada game pada inventory-mu yang memenuhi kriteria")

    elif isFilled(year):

        year = int(year)
        matched = []

        for j in foundgame:
            if j[3] == year:
                matched += [j]
                
        if isFilled(matched):
            print("Daftar game pada inventory yang memenuhi kriteria:")
            r.neatList(matched, False)
        else:
            print("Daftar game pada inventory yang memenuhi kriteria:")
            print("Tidak ada game pada inventory-mu yang memenuhi kriteria")

    else:
        print("Daftar game pada inventory-mu:")
        r.neatList(foundgame, False)

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
# cariGameInventory(loginData[0], datagame, datakep)
# for i in datagame:
#     print(i)