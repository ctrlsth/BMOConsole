# Main Program - Tugas Besar Dasar Pemrograman IF1210 K01-13

# Program BiNoMO
import rCSV as r; import argparse; import os; import time; import sys
import F02, F03, F04, F05, F06, F07, F08, F09, F10, F11, F12, F13, F14, F15, F16, F17, B02, B03

# Main Loop
def mainloop():

    global role
    global logged_in, changes
    global logged_user
    global datauser, headeruser
    global datagame, headergame
    global datakep, headerkep
    global datahis, headerhis

    query = input(">>> ")
    query = query.lower()

    modifyingFunctions = ["register", "tambah_game", "ubah_game", "ubah_stok", "topup", "beli_game"]
    
    if role == "user":
        if query == modifyingFunctions[5]:
            changes = True
    elif role == "admin":
        for h in range (5):
            if query == modifyingFunctions[h]:
                changes = True

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


    # F08 - Membeli Game
    elif query == "beli_game":
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

    # F16 - Save
    elif query == "save":
        if logged_in:
            folder = input("Masukan nama folder penyimpanan: ")
            callSave(folder)
            time.sleep(1.5)
        else:
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”')

        print()
        mainloop()
    

    # F17 - Exit { Blm gw pake yg Fun   gsinya }
    elif query == "exit":
        out = input("Apakah anda ingin keluar dari program? (y/n) ")
        if out.upper() == "Y":
            if logged_in and changes:
                save = F17.exit()
                if save:
                    folder = input("Masukan nama folder penyimpanan: ")
                    callSave(folder)
                    time.sleep(1.5)
                
            print("Menutup program...")
            time.sleep(1)
        
            time.sleep(3)
            os.system('cls')
            sys.exit()
        
        elif out.upper() == "N":
            print()
            mainloop()
        
        else:
            print("Masukkan tidak valid")
            print()
            mainloop()


    # B02 - Magic Conch Shell
    elif query == "kerangajaib":
        if logged_in:
            B02.kerangajaib()
        else:
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”')

        print()
        mainloop()


    # B03 - Tic Tac Toe
    elif query == "tictactoe":
        if logged_in:
            B03.tictactoe()
        else:
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”')

        print()
        mainloop()


    # Error - Jika masukan command tidak terdefinisi
    else:
        print("Tidak ada command seperti itu!")
        print('Gunakan command "help" untuk melihat list command')
        print()
        mainloop()

    return

    # Yang Belum:
    # elif query == "kerang ajaib"
    

def callSave(folder):

    global datauser, headeruser
    global datagame, headergame
    global datakep, headerkep
    global datahis, headerhis

    F16.save(folder, headergame, datagame, "game")
    F16.save(folder, headeruser, datauser, "user")
    F16.save(folder, headerkep, datakep, "kepemilikan")
    F16.save(folder, headerhis, datahis, "riwayat")

    return

##################################################

# PROGRAM EXECUTION
# Global Variables
# # Intialize Data Matrixes
datauser = []
headeruser = []

datagame = []
headergame = []

datakep = []
headerkep = []

datahis = []
headerhis = []

# # Login Data
changes = False
logged_in = False
role = ""
logged_user = []

# ALGORITHM
# Asking for CSV Files Directory
parser = argparse.ArgumentParser()
parser.add_argument("folder", help="Input harus menyertakan folder")
args = parser.parse_args()
dirf = args.folder

# Loading
if not os.path.exists(dirf): 
    print(f'Folder "{dirf}" tidak ditemukan')
    print()
else:
    F15.load(dirf, datauser, headeruser, "user")
    F15.load(dirf, datagame, headergame, "game")
    F15.load(dirf, datakep, headerkep, "kepemilikan")
    F15.load(dirf, datahis, headerhis, "riwayat")

    # Jalanin Program
    mainloop()