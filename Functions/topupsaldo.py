# F12
import rCSVkay

datau = []                                 
use = open("/Users/kayleenchristopher/F09F12/user.csv","r")
use_name = "user"
rawu_lines = use.readlines()
use.close()
cleanes = rCSVkay.todata(rawu_lines, datau, use_name)
headers = cleanes[0]

inputuser = str(input("Masukan username: "))
topupsaldo = int(input("Masukan saldo: "))
valid = False

for i in datau:
    if(i[1] == inputuser):
        if((topupsaldo + i[5]) < 0):
            print("Masukan tidak valid.")
        else:
            i[5] = i[5] + topupsaldo
            saldoakhir = i[5]
            name = i[2]
        valid = True
        break
    else:
        valid = False

if not valid:
    print("Username", inputuser, "tidak ditemukan.")
else:
    if (topupsaldo < 0):
        print("Top up berhasil. Saldo", name, "berkurang menjadi", saldoakhir,".")
    else:
        print("Top up berhasil. Saldo", name, "bertambah menjadi", saldoakhir,".")


# To do for F12 : Baca file user.csv, tampung semua data di array, check user yang mana yang mau top up saldo, baca saldo,
#tambahin saldo ke array, tulis lagi semuanya ke csv
# Question : Apakah harus ulang input lagi kalau salah input username?
