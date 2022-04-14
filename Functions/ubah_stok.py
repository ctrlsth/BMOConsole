def ubahStok (id, jumlah, cekid, datagame):

    id = input('Masukkan ID: ')
    jumlah = int(input('Masukkan jumlah: '))
    cekid = False

    for i in datagame:
        if i[0] == id :
            ubahstok = i[5] + jumlah
            if ubahstok >= 0 :
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