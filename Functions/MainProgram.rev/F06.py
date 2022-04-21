def ubahStok (datagame):

    id = input('Masukkan ID game: ')
    jumlah = int(input('Masukkan jumlah: '))
    cekid = False

    for i in datagame:
        if i[0] == id :
            ubahstok = i[5] + jumlah
            # print(i)
            if ubahstok >= 0 :
                i[5] = ubahstok
                if ubahstok < i[5]:
                    print(f"Stok game {i[1]} berhasil dikurangi. Stok sekarang: {ubahstok}")
                elif ubahstok >= i[5]:
                    print(f"Stok game {i[1]} berhasil ditambahkan. Stok sekarang: {ubahstok}")
                cekid = True
                break
            else : 
                print(f"Stok game {i[1]} gagal dikurangi karena stok kurang. Stok sekarang: {i[5]}")
                cekid = True
                break
                  
    if cekid == False :
        print("Tidak ada game dengan ID tersebut")
    
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
# ubahStok(datagame)
# for i in datagame:
#     print(i)