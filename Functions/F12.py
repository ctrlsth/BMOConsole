# import DummyLoad as l

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


# F12 - Topup Saldo

# Prosedur
def topup(datauser):

    username = input("Masukan username: ")
    topupsaldo = int(input("Masukan saldo: "))
    valid = False

    for i in datauser:
        if(i[1] == username):
            valid = True
            if((topupsaldo + i[5]) < 0):
                print("Masukan tidak valid.")
                break
            else:
                i[5] = i[5] + topupsaldo
                saldoakhir = i[5]
                name = i[2]

                if (topupsaldo < 0):
                    print("Top up berhasil. Saldo", name, "berkurang menjadi", saldoakhir,".")
                else:
                    print("Top up berhasil. Saldo", name, "bertambah menjadi", saldoakhir,".")
                break
            
    if not valid:
        print('Username "' + username + '" tidak ditemukan.')

    return

# Test Case
# topup(datauser)
# for i in datauser:
#     if i[0] == 2:
#         print(i)
