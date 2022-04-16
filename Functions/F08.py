# F08 - Membeli Game

import rCSV as r
import f03 as l

# riwayat.csv
header = []
data = []
f = open("C:/Users/Alka/riwayat.csv","r")   
csv_name = "riwayat"     
raw_lines = f.readlines()                   
f.close()                                       
csvtuple = r.todata(raw_lines, header, data, csv_name)      

# kepemilikan.csv
header2 = []
data2 = []
f2 = open("C:/Users/Alka/kepemilikan.csv","r")   
csv_name2 = "kepemilikan"     
raw_lines2 = f2.readlines()                   
f2.close()                                       
csvtuple2 = r.todata(raw_lines2, header2, data2, csv_name2)     

# game.csv
header3 = []
data3 = []
f3 = open("C:/Users/Alka/game.csv","r")   
csv_name3 = "game"     
raw_lines3 = f3.readlines()                   
f3.close()                                       
csvtuple3 = r.todata(raw_lines3, header3, data3, csv_name3)

# login dulu mungkin? Cara dapet data login kyk gini kah?
loginValid, loginData = l.login()
# print(loginData)

# ada if (role == "user") disini mungkin?
def buy_game() :
    in_gameid = str(input("Masukkan ID Game: "))
    new_riw = []
    new_kep = []
    owned = False
    

#     for i in data :
#         if (loginData[1] == i[3]) :
#             new_riw += [i]

    for j in data2 :
        if (int(loginData[0]) == int(j[1])) :
            new_kep += [j]
    for j in new_kep :                    
        if (in_gameid == j[0]) :
            print("Anda sudah memiliki Game tersebut!")
            owned = True # ga harus break kan ya soalnya gamungkin punya game yg sama
            
    if not (owned) :
        for k in data3 :
            if ((in_gameid) == (k[0])) :
                new_game = k
        if (loginData[5] < new_game[4]) :
            print("Saldo anda tidak cukup untuk membeli Game tersebut!")
        elif (new_game[5] <= 0) :
            print("Stok Game tersebut sedang habis!")
        else :
            loginData[5] -= new_game[4] # ngurangin saldo
            new_riw += [[in_gameid, loginData[2], new_game[4], loginData[1], 2022]] # nambahin riwayat game
            new_kep += [[in_gameid, loginData[0]]] # nambahin kepemilikan game
            new_game[5] -= 1 # ngurangin stok game
            print("Game “" + new_game[1] + "” berhasil dibeli!")
    # print(loginData) 
    # print(new_riw)
    # print(new_kep)
    # print(new_game)

# loginData[0-5] itu dari user.csv
# new_game[0-5] itu dari game.csv

# buy_game() # buat ngecek doang
