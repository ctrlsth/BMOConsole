import rCSV_rev2 as r

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

def cariGameInventory(logged_in, datagame, datakep):
# prosedur: Menampilkan list game dari inventory seorang user berdasarkan hasil pencarian

# KAMUS LOKAL
# parameters
    # logged_in : int
    # datagame : matrix
    # datakep : matrix of str
# variables
    # idgame, year : str
    # foundgame, matched : matrix

# ALGORITMA
    idgame = input("Masukkan ID Game: ")
    year = input("Masukkan Tahun Rilis Game: ")

    foundgame = []
    for line in datakep:
        if line[1] == logged_in:
            for i in datagame:
                if i[0] == line[0]:
                    foundgame += [i]
                    break


    if isFilled(idgame):

        matched = []
        for game in foundgame:
            if game[0] == idgame:
                matched += [game]

        if isFilled(matched):
            if isFilled(year):
                year = int(year)
                print("Daftar game pada inventory yang memenuhi kriteria:")
                if year == foundgame[0][3]:
                    r.neatList(foundgame, False)
                else:
                    print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
            else:
                print("Daftar game pada inventory yang memenuhi kriteria:")
                r.neatList(foundgame, False)
        else:
            print("Daftar game pada inventory yang memenuhi kriteria:")
            print("Tidak ada game pada inventory-mu yang memenuhi kriteria")

    elif isFilled(year):

        year = int(year)
        
        for j in foundgame:
            if j[3] == year:
                print("Daftar game pada inventory yang memenuhi kriteria:")
                r.neatList(foundgame, False)
            else:
                print("Daftar game pada inventory yang memenuhi kriteria:")
                print("Tidak ada game pada inventory-mu yang memenuhi kriteria")

    else:
        print("Daftar game pada inventory-mu:")
        r.neatList(foundgame, False)

    return