import rCSV as r
import f03 as l

# Baca csv

# riwayat.csv
header = []
data = []
f = open("C:/Users/Alka/riwayat.csv","r")   
csv_name = "riwayat"     
raw_lines = f.readlines()                   
f.close()                                       
csvtuple = r.todata(raw_lines, header, data, csv_name)      
header = []

# game.csv
header2 = []
data2 = []
f2 = open("C:/Users/Alka/game.csv","r")   
csv_name2 = "game"     
raw_lines2 = f2.readlines()                   
f2.close()                                       
csvtuple2 = r.todata(raw_lines2, header2, data2, csv_name2)      


# ini juga butuh data login buat ngeceknya kyknya (?)
loginValid, loginData = l.login()
# print(loginData)

betterheader = ["ID Game", "Nama Game", "Kategori (Genre)", "Tahun Rilis", "Harga", "Stok"]
print()

riw = []

for j in data :
    if ((int(loginData[0])) == int(j[3]) ) :
        for i in data2 :
            if (i[0] == j[0]) :
                riw += [i]

print(riw)
if (riw == []):
    print("Maaf, kamu belum membeli riwayat. Ketik perintah beli_game untuk beli.")
else:
    print("Daftar riwayat : ")
    wordlength = r.findLongest(riw)
    r.neatList(riw, False)
# harusnya sama kyk f09, cuman bedanya f09 kepemilikan & f13 riwayat
