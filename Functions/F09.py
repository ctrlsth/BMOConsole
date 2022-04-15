# F09 - Melihat Game yang dimiliki
import rCSVk

# UNTUK MEMBACA
datag = []
headerg = []
csv = open("/Users/kayleenchristopher/F09F12/game.csv","r")
csv_name = "game"
raw_lines = csv.readlines()
csv.close()
rCSVk.todata(raw_lines, headerg, datag, csv_name)


datakepemilikan = []
headerkep = []
kep = open("/Users/kayleenchristopher/F09F12/kepemilikan.csv","r")
kep_name = "kepemilikan"
rawk_lines = kep.readlines()
kep.close()
rCSVk.todata(rawk_lines, headerkep, datakepemilikan, kep_name)


datauser = []
headeruser = []
use = open("/Users/kayleenchristopher/F09F12/user.csv","r")
use_name = "user"
rawu_lines = use.readlines()
use.close()
rCSVk.todata(rawu_lines, headeruser, datauser, use_name)


# UNTUK FORMAT OUTPUT

betterheader = ["ID Game", "Nama Game", "Kategori (Genre)", "Tahun Rilis", "Harga", "Stok"]
print()

usergame = []
i = 0
valid = False

inputuserid = str(input("Silakan input username Anda: "))

for k in datauser:
    if(k[1] == inputuserid):
        userid = k[0]
        valid = True
        break
if not valid:
    print("Username tidak ditemukan.")
else:
    for j in datakepemilikan:
        if(j[1] == userid):
            for x in datag:
                if(x[0] == j[0]):
                    usergame += [[x[0], x[1], x[2], x[3], x[4], x[5]]]
                    valid = True
                    break
                else:
                    valid = False
    if not valid:
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
    else:
        print("Daftar game : ")
        wordlength = rCSVk.findLongest(usergame)
        rCSVk.neatList(usergame, False)
# Question : Apakah harus ulang input lagi kalau salah input username?
