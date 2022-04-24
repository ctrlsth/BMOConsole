# # Initialize
# import DummyLoad as l

# # Inisiasi
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

# F09 - Melihat Game yang dimiliki
import rCSV as r

def list_kep(datagame, datakep, userid):

    usergame = []
    valid = False

    for j in datakep:
        if(j[1] == userid):
            for x in datagame:
                if(x[0] == j[0]):
                    usergame += [[x[0], x[1], x[2], x[3], x[4], x[5]]]
                    valid = True
                    break
                else:
                    valid = False
    if not valid:
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
    else:
        r.neatList(usergame, False)

    return

# # Test Case
# list_kep(datagame, datakep, loginData[0])