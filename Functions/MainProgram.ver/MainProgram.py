
import rCSV as r
import F02, F03, F04, F05, F06, F07, F08, F09, F10, F11, F12, F13, F14
import DummyLoad as l

# Inisiasi Memori
headeruser = []
datauser = []
l.user(headeruser, datauser)

headergame = []
datagame = []
l.game(headergame, datagame)

headerkep = []
datakep = []
l.kepemilikan(headerkep, datakep)

headerhis = []
datahis = []
l.riwayat(headerhis, datahis)

logged_in = False
role = ""
logged_user = []

# Main Loop
def mainloop():

    global role
    global logged_in
    global logged_user

    query = input(">>> ")

    # F03 - Login 
    if query == "login":
        if logged_in == False:
            logged_user += F03.login(datauser)
            if r.length(logged_user) != 0:
                role = logged_user[4]
                logged_in = True
        else:
            print("Anda sudah berhasil login.")
        
        print()
        mainloop()


    # F02 - Register
    elif query == "register":
        if logged_in and role == "admin":
            F02.register(datauser)
        else:
            if logged_in == False:
                print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”')
            elif role != "admin":
                print('Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.')

        print()
        mainloop()


    # F04 - Menambah Game ke Toko Game
    elif query == "tambah_game":
        if logged_in and role == "admin":
            F04.newGame(datagame)
        else:
            if logged_in == False:
                print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”')
            elif role != "admin":
                print('Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.')

        print()
        mainloop()


    # F05 - Mengubah Game pada Toko Game
    elif query == "ubah_game":
        if logged_in and role == "admin":
            F05.modGameStore(datagame)
        else:
            if logged_in == False:
                print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”')
            elif role != "admin":
                print('Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.')
    
        print()
        mainloop()


    # F06 - Mengubah Stok Game di Toko
    elif query == "ubah_stok":
        if logged_in and role == "admin":
            F06.ubahStok(datagame)
        else:
            if logged_in == False:
                print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”')
            elif role != "admin":
                print('Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.')
    
        print()
        mainloop()


    # F07 - Listing Game di Toko Berdasarkan ID, Tahun Rilis dan Harga
    elif query == "list_game_toko":
        if logged_in:
            F07.listgame(datagame)
        else:
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”')

        print()
        mainloop()


    # F08 - Membeli Game { B }
    elif query == "buy_game":
        if logged_in and role == "user":
            F08.buy_game(datauser, datagame, datahis, datakep, logged_user)
        else:
            if logged_in == False:
                print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”')
            elif role != "user":
                print('Maaf, anda harus menjadi user untuk melakukan hal tersebut.')

        print()
        mainloop()


    # F09 - Melihat Game yang dimiliki
    elif query == "list_game":
        if logged_in and role == "user":
            F09.list_kep(datagame, datakep, logged_user[0])
        else:
            if logged_in == False:
                print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”')
            elif role != "user":
                print('Maaf, anda harus menjadi user untuk melakukan hal tersebut.')

        print()
        mainloop()

    # F10 - Mencari Game yang dimiliki dari ID dan tahun rilis
    elif query == "search_my_game":
        if logged_in and role == "user":
            F10.cariGameInventory(logged_user[0], datagame, datakep)
        else:
            if logged_in == False:
                print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”')
            elif role != "user":
                print('Maaf, anda harus menjadi user untuk melakukan hal tersebut.')

        print()
        mainloop()


    # F11 - Mencari Game di Toko dari ID, Nama Game, Harga, Kategori dan Tahun Rilis 
    elif query == "search_game_at_store":
        if logged_in:
            F11.searchGame(datagame)
        else:
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”')

        print()
        mainloop()
    

    # F12 - Topup Saldo
    elif query == "topup":
        if logged_in and role == "admin":
            F12.topup(datauser)
        else:
            if logged_in == False:
                print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”')
            elif role != "admin":
                print('Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.')
    
        print()
        mainloop()


    # F13 - Melihat Riwayat Pembelian
    elif query == "riwayat":
        if logged_in and role == "user":
            F13.showriwayat(datahis, datagame, logged_user[0])
        else:
            if logged_in == False:
                print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”')
            elif role != "user":
                print('Maaf, anda harus menjadi user untuk melakukan hal tersebut.')

        print()
        mainloop()


    # F14 - Help
    elif query == "help":
        F14.help(role)

        print()
        mainloop()
    

    # F17 - Exit { Blm gw pake yg Fungsinya }
    elif query == "exit":
        print("BMO Logged Off")
        print()


    # Error - Jika masukan command tidak terdefinisi
    else:
        print("Tidak ada command seperti itu!")
        print('Gunakan command "help" untuk melihat list command')
        print()
        mainloop()

mainloop()
    
    # load()
    
    # elif query == "riwayat"
    # elif query == "save"
    


    