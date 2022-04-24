import os
import rCSV as r
import time

userflag = False
gameflag = False
hisflag = False
kepflag = False
delflag = False

def save(folder, header, data, csv_name): 
    
    global userflag, gameflag, hisflag, kepflag, delflag

    if not delflag:
        if not os.path.exists(folder):
            os.makedirs(folder)
        for (root,dirs,files) in os.walk(folder, topdown=False):
            for f in files :
                os.remove(f'{folder}\\{f}')

        delflag = True

    if csv_name == "user":
        with open(folder + "\\user.csv", "w+") as g:
            g.write(r.saving(header, data))
        userflag = True

    elif csv_name == "game":
        with open(folder + "\\game.csv", "w+") as g:
            g.write(r.saving(header, data))
        gameflag = True

    elif csv_name == "riwayat":
        with open(folder + "\\riwayat.csv", "w+") as g:
            g.write(r.saving(header, data))
        hisflag = True

    elif csv_name == "kepemilikan":
        with open(folder + "\\kepemilikan.csv", "w+") as g:
            g.write(r.saving(header, data))
        kepflag = True

    if userflag and gameflag and kepflag and hisflag:
        print('Saving...')
        time.sleep(2)
        print("Data telah disimpan pada folder " + folder + "!")
    
        delflag = False
        userflag = False
        gameflag = False
        hisflag = False
        kepflag = False