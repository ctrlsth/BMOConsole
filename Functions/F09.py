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


# # UNTUK FORMAT OUTPUT

# csv_name1 = "game"
# csv_name2 = "kepemilikan"

# gamedata = []
# headergame = []
# rCSVk.todata(raw_lines, headergame, gamedata, csv_name1)

# kepdata = []
# headerkepemilikan = []
# rCSVk.todata(rawk_lines, headerkepemilikan, kepdata, csv_name2)

betterheader = ["ID Game", "Nama Game", "Kategori (Genre)", "Tahun Rilis", "Harga", "Stok"]
# print()

usergame = []
i = 0
valid = False

inputuserid = str(input("Silakan input username Anda:")) # Bikin dummy aja jd ga minta input and user_id itu integer

for j in datakepemilikan:
    if(j[1] == inputuserid):
        for x in datag:
            if(x[0] == j[0]):
                usergame += [[x[0], x[1], x[2], x[3], x[4]]] # gw rasa langsung kek x aja juga bisa but idk have to tryit
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
