import rCSV as r
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

# loginData = [3, "hanhan","Hans", "snah", "user", 20000]

def showriwayat(datahis, datagame, user_id):

    riw = []
    temphis = []
    for line in datahis:
        if line[3] == user_id:
            for game in datagame:
                if game[0] == line[0]:
                    temphis += [game[0], game[1]]
            temphis += [line[2], line[4]]
            riw += [temphis]
            temphis = []
    
    if riw == []:
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
    else:
        print("Daftar riwayat : ")
        r.neatList(riw, False, True)

    return

# Test Case
# neatHis(datahis, datagame, loginData[0])