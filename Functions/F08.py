# F08 - Membeli Game

import rCSV_rev as r
import f03 as l

# kepemilikan.csv
data2 = []
f2 = open("C:/Users/Alka/kepemilikan.csv","r")   
csv_name2 = "kepemilikan"     
raw_lines2 = f2.readlines()                   
f2.close()                                       
csvtuple2 = r.todata(raw_lines2, data2, csv_name2)      
header2 = csvtuple2[0]

# game.csv
data3 = []
f3 = open("C:/Users/Alka/game.csv","r")   
csv_name3 = "game"     
raw_lines3 = f3.readlines()                   
f3.close()                                       
csvtuple3 = r.todata(raw_lines3, data3, csv_name3)      
header3 = csvtuple3[0]

# login dulu mungkin? Cara dapet data login kyk gini kah?
loginValid, loginData = l.login()
# print(loginData)

# ada if (role == "user") disini mungkin?
def buy_game() :
    id = loginData[0]
    saldo = loginData[5]
    in_gameid = str(input("Masukkan ID Game: "))

    for i in data2 :
        if (int(id) == int(i[1])) :            
            if (in_gameid == i[0]) :
                print("Anda sudah memiliki Game tersebut!")
                break
            for j in data3 :
                # print(in_gameid) buat ngecek doang
                # print(j[0]) buat ngecek doang
                if ((in_gameid) == (j[0])) :
                    # print(j) buat ngecek doang
                    nama_game = j[1]
                    harga = j[4]
                    stok = j[5]
            # print(harga) buat ngecek doang
            if (saldo < harga) :
                print("Saldo anda tidak cukup untuk membeli Game tersebut!")
                break
            elif (stok <= 0) :
                print("Stok Game tersebut sedang habis!")
                break
            else :
                print("Game “",nama_game,"” berhasil dibeli!")  # output di nama_gamenya msh ada spasinya, jadi ga sama persis kyk di spesifikasi
                saldo = saldo - harga
                stok -= 1
                break
                # belom tambahin game tersebut ke riwayat tahun dibeli 2022 + kepemilikan
        # kalo misal in_gameid gaada gmn? gaada di spesifikasi

# tulis kode buat modif sama saving disini juga kah? *confusion*

# buy_game() # buat ngecek doang