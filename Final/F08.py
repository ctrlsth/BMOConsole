# import DummyLoad as l
from datetime import date

# Inisiasi
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

# Prosedur
def buy_game(datauser, datagame, datahis, datakep, loginData) :
    
    in_gameid = input("Masukkan ID Game: ")
    new_riw = []
    new_kep = []
    new_game = []
    owned = False
    found = False

    for i in datagame:
        if i[0] == in_gameid:
            found = True
            break

    if found:
        for j in datakep :
            if (j[1] == loginData[0]) and (in_gameid == j[0]):
                print("Anda sudah memiliki Game tersebut!")
                owned = True
                break

        if not owned :
        
                for k in datagame :
                    if (in_gameid == k[0]) :
                        new_game += k

                if (new_game[5] <= 0) :
                    print("Stok Game tersebut sedang habis!")
                elif (loginData[5] < new_game[4]) :
                    print("Saldo anda tidak cukup untuk membeli Game tersebut!")
                else :
                    loginData[5] -= new_game[4] # ngurangin saldo
                    for l in datauser:
                        if l[0] == loginData[0]:
                            l[5] = loginData[5]

                    new_riw += [[in_gameid, loginData[2], new_game[4], loginData[0], date.today().year]] # nambahin riwayat game
                    datahis += new_riw

                    new_kep += [[in_gameid, loginData[0]]] # nambahin kepemilikan game
                    datakep += new_kep

                    new_game[5] -= 1 # ngurangin stok game
                    for m in datagame:
                        if m[0] == in_gameid:
                            m[5] = new_game[5]

                    print("Game “" + new_game[1] + "” berhasil dibeli!")

    else:
        print("ID Game tidak ditemukan!")
    
    return 

# test case {hans}
# buy_game(datauser, datagame, datahis, datakep, loginData)
# for i in datahis:
#     print(i)
# for j in datakep:
#     print(j)


# Loop Test Case
# loop = True
# while loop:
#     A = int(input("loop : "))
#     if A == 1:
#         buy_game(datauser, datagame, datahis, datakep, loginData)
#         for data in datahis:
#             if data[3] == 2:
#                 print(data)
#         print()
#         for datas in datakep:
#             if datas[1] == 2:
#                 print(datas)
#         print()
#         for datass in datauser:
#             if datass[0] == 2:
#                 print(datass)
#         print()
#         print("Login Data:")
#         print(loginData)
#         print()
#     else:
#         loop = False

    # print(loginData) 
    # print(new_riw)
    # print(new_kep)
    # print(new_game)

# loginData[0-5] itu dari user.csv
# new_game[0-5] itu dari game.csv

# buy_game() # buat ngecek doang