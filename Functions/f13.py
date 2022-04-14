import rCSV_rev as r
import f03 as l

# Baca csv
# game.csv
data = []
f = open("C:/Users/Alka/game.csv","r")   
csv_name = "game"     
raw_lines = f.readlines()                   
f.close()                                       
csvtuple = r.todata(raw_lines, data, csv_name)      
header = csvtuple[0]

# riwayat.csv
data2 = []
f2 = open("C:/Users/Alka/riwayat.csv","r")   
csv_name2 = "riwayat"     
raw_lines2 = f2.readlines()                   
f2.close()                                       
csvtuple2 = r.todata(raw_lines2, data2, csv_name2)      
header2 = csvtuple2[0]


# ini juga butuh data login buat ngeceknya kyknya (?)
loginValid, loginData = l.login()
print(loginData)
user_id = loginData[1] # di csv riwayat yg "id" mungkin harusnya yg 1,2,3,4,5 tpi ini gw pake username nya jadi

# UNTUK FORMAT OUTPUT
game_data = []
res = r.todata(raw_lines, game_data, csv_name)
headergame = res[0]

riw_data = []
res2 = r.todata(raw_lines2, riw_data, csv_name2)
header_riw = res2[0]

betterheader = ["ID Game", "Nama Game", "Kategori (Genre)", "Tahun Rilis", "Harga", "Stok"]
print()

usergame = []
i = 0
valid = False

for j in data2:
    print(j[3])
    if(user_id == j[3]):
        for i in data:
            if(i[0] == j[0]):
                usergame += [[i[0], i[1], i[2], i[3], i[4]]]
                valid = True
                break
            else:
                valid = False
if not valid:
    print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
else:
    print("Daftar game : ")
    wordlength = r.findLongest(usergame)
    r.neatList(betterheader, usergame, wordlength)
# harusnya sama kyk f09, cuman bedanya f09 kepemilikan & f13 riwayat