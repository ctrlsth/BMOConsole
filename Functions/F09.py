# F09 - listgame.py
import rCSVkay

userid = "kaykay"

# UNTUK MEMBACA
datag = []                                 
csv = open("/Users/kayleenchristopher/F09F12/game.csv","r")
csv_name = "game"
raw_lines = csv.readlines()
csv.close()
clean = rCSVkay.todata(raw_lines, datag, csv_name)
header = clean[0]

datakepemilikan = []
kep = open("/Users/kayleenchristopher/F09F12/kepemilikan.csv","r")
kep_name = "kepemilikan"
rawk_lines = kep.readlines()
kep.close()
cleans = rCSVkay.todata(rawk_lines, datakepemilikan, kep_name)
heads = cleans[0]

# UNTUK FORMAT OUTPUT

csv_name1 = "game"
csv_name2 = "kepemilikan"

gamedata = []
res = rCSVkay.todata(raw_lines, gamedata, csv_name1)
headergame = res[0]

kepdata = []
res2 = rCSVkay.todata(rawk_lines, kepdata, csv_name2)
headerkepemilikan = res2[0]

betterheader = ["ID Game", "Nama Game", "Kategori (Genre)", "Tahun Rilis", "Harga", "Stok"]
print()

usergame = []
i = 0
valid = False

inputuserid = str(input("Silakan input username Anda:"))

for j in datakepemilikan:
    if(j[1] == inputuserid):
        for x in datag:
            if(x[0] == j[0]):
                usergame += [[x[0], x[1], x[2], x[3], x[4]]]
                valid = True
                break
            else:
                valid = False
if not valid:
    print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
else:
    print("Daftar game : ")
    wordlength = rCSVkay.findLongest(usergame)
    rCSVkay.neatList(betterheader, usergame, wordlength)
# Question : Apakah harus ulang input lagi kalau salah input username?