import rCSVk

datau = []
headeru = []
use = open("/Users/kayleenchristopher/F09F12/user.csv","r")
use_name = "user"
rawu_lines = use.readlines()
use.close()
cleanes = rCSVk.todata(rawu_lines, headeru, datau, use_name)

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

# Question : Apakah harus ulang input lagi kalau salah input username?
