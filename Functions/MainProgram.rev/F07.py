# F07 - Listing Game di toko
import rCSV as r

def listgame(datagame):
    

    print("List Skema Sorting: ")
    print("- tahun+")
    print("- tahun-")
    print("- harga+")
    print("- harga-")
    print("- urut (tidak perlu memasukkan input)")
    print()
    skema = input('Skema sorting: ')
    

    y = r.copy(datagame)
    x = r.length(datagame)
    if skema == 'tahun-' :
        for i in range(x-1):
            for j in range(0,x-i-1):
                if (y[j][3]) < (y[j+1][3]) :
                    y[j], y[j+1] = y[j+1], y[j]
        r.neatList(y, True)
    elif skema == 'tahun+' :
        for i in range(x-1):
            for j in range(0,x-i-1):
                if (y[j][3]) > (y[j+1][3]) :
                    y[j], y[j+1] = y[j+1], y[j]
        r.neatList(y, True)
    elif skema == 'harga+' :
        for i in range(x-1):
            for j in range(0,x-i-1):
                if (y[j][4]) > (y[j+1][4]) :
                    y[j], y[j+1] = y[j+1], y[j]
        r.neatList(y, True)
    elif skema == 'harga-' :  
        for i in range(x-1):
            for j in range(0,x-i-1):
                if (y[j][4]) < (y[j+1][4]) :
                    y[j], y[j+1] = y[j+1], y[j]
        r.neatList(y, True)
    elif skema == '':
        for i in range(x-1):
            for j in range(0,x-i-1):
                if (y[j][0][4]) < (y[j+1][0][4]) :
                    y[j], y[j+1] = y[j], y[j+1]
                elif (y[j][0][4]) > (y[j+1][0][4]):
                    y[j], y[j+1] = y[j+1], y[j]
                else:
                    if (y[j][0][5]) < (y[j+1][0][5]) :
                        y[j], y[j+1] = y[j], y[j+1]
                    elif (y[j][0][5]) > (y[j+1][0][5]):
                        y[j], y[j+1] = y[j+1], y[j]
                    else:
                        if (y[j][0][6]) < (y[j+1][0][6]) :
                            y[j], y[j+1] = y[j], y[j+1]
                        elif (y[j][0][6]) > (y[j+1][0][6]):
                            y[j], y[j+1] = y[j+1], y[j]
                        else:
                            y[j], y[j+1] = y[j], y[j+1]
        r.neatList(y, True)
    else:
        print("Skema sorting tidak valid!")
    
    return

# test case
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

# # manggil fungsi
# listgame(datagame)