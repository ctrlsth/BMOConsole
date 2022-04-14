id11 = input('Masukkan ID Game: ')
name11 = input('Masukkan Nama Game: ')
kategori11 = input('Masukkan Kategori Game: ')
tahun11 = input('Masukkan Tahun Rilis Game: ')
harga11 =input('Masukkan Harga Game: ')
cek = 0
list= []

        
for i in datagame:
    if (i[0] == id11 or i[0] == ' ') :
        if (i[1] == name11 or i[1] == '' ) :
            if (i[2] == kategori11 or i[2] == ''):
                if (i[3] == tahun11 or i[3] == '' ):
                    if (i[4] == harga11 or i[4] == ''):
                        list += [i]
                        cek += 1
        
if cek == 0 :
    print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
else :
    print('Daftar game pada inventory yang memenuhi kriteria:')
    for i in list:
        print(i)