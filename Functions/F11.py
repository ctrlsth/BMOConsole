
def searchGame (datagame):
    id11 = input('Masukkan ID Game: ')
    name11 = input('Masukkan Nama Game: ')
    kategori11 = input('Masukkan Kategori Game: ')
    tahun11 = input('Masukkan Tahun Rilis Game: ')
    harga11 =input('Masukkan Harga Game: ')
    cek = 0
    list= []

        
    for i in datagame:
        if (i[0] == id11 or id11 == '') :
            if (i[1] == name11 or name11 == '' ) :
                if (i[2] == kategori11 or kategori11 == ''):
                    if (i[3] == tahun11 or tahun11 == '' ):
                        if (i[4] == harga11 or harga11 == ''):
                            list += [i]
                            cek += 1
        
    if cek == 0 :
        print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
    else :
        print('Daftar game pada inventory yang memenuhi kriteria:')
        for i in list:
            print(i)
            
array = [['GAME102', 'ITB Crossing', 'Role-playing', '2000' , '100000', '5'], ['GAME067', 'Laprak Rhapsody', 'Survival and horror', '2010' , '60000', '4'], ['GAME127', 'Daigakusei no Seikatsu', 'Real-time Strtegy', '2015' , '75000', '6']]

searchGame(array)