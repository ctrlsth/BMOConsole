# F03 - Login
import rCSV as r

def login(datauser) :
    
    loginValid = False
    in_username = input("Masukan username: ")
    in_password = input("Masukan password: ")
    loginData = []

    for i in datauser :
        if (in_username == i[1] and in_password == i[3]) :
            nama = i[2]
            loginData += i
            loginValid = True
    if loginValid :
        print("Halo, " + nama + "! Selamat datang di “Binomo”.") 
    else : # if not loginValid :
        print("Password atau username salah atau tidak ditemukan.")
    
    return loginData
        

# # test case
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

# manggil fungsi
# login(datauser)