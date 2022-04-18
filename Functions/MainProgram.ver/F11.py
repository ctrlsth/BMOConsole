import rCSV as r

def searchGame (datagame):
    id11 = input('Masukkan ID Game: ')
    name11 = input('Masukkan Nama Game: ')
    kategori11 = input('Masukkan Kategori Game: ')
    tahun11 = (input('Masukkan Tahun Rilis Game: '))
    harga11 = (input('Masukkan Harga Game: '))
    cek = 0
    list= []

        
    for i in datagame:
        if (i[0] == id11 or id11 == '') :
            if (i[1] == name11 or name11 == '') :
                if (i[2] == kategori11 or kategori11 == ''):
                    if (str(i[3]) == tahun11 or tahun11 == '' ):
                        if (str(i[4]) == harga11 or harga11 == ''):
                            list += [i]
                            cek += 1
        
    if cek == 0 :
        print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
    else :
        print()
        print('Daftar game pada inventory yang memenuhi kriteria:')
        r.neatList(list,True)
            
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
# searchGame(datagame)
# for i in datagame:
#     print(i)