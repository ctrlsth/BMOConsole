# F15 - Load

import rCSV as r ; import time ; import os

userflag = False
gameflag = False
hisflag = False
kepflag = False

def load(dirf, data, header, csv_name) :

    global userflag, gameflag, hisflag, kepflag
    
    if csv_name == "user":
        with open(dirf + "\\user.csv", "r") as f: 
            raw_lines = f.readlines()
            f.close()
            r.todata(raw_lines, header, data, csv_name)
        userflag = True

    elif csv_name == "game":
        with open(dirf + "\\game.csv", "r") as g: 
            raw_lines = g.readlines()
            g.close()
            r.todata(raw_lines, header, data, csv_name)
        gameflag = True

    elif csv_name == "riwayat":
        with open(dirf + "\\riwayat.csv", "r") as h: 
            raw_lines = h.readlines()
            h.close()
            r.todata(raw_lines, header, data, csv_name)
        hisflag = True

    elif csv_name == "kepemilikan":
        with open(dirf + "\\kepemilikan.csv", "r") as e: 
            raw_lines = e.readlines()
            e.close()
            r.todata(raw_lines, header, data, csv_name)
        kepflag = True

    if kepflag and hisflag and gameflag and userflag:
        
        print()
        time.sleep(1)
        print("Memuat Antarmuka...")
        time.sleep(2)
        print('''
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@%**@@@@@@@@@++%@@@@@@@*+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@%:::=@@@@@@@%  *@@@@@@%  -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@%::::%@@@@@@@%  +#*#@@@@#*%@@@%**#@@@@@@#**%@@@@@%**#@@#**%@@@@@%**#@@@@@@@@@@@@
        @@@@@@@@@%::::%%++%@@@@%    .  =@@  =@@:     =@@+  .  .*@@-    .     -@@*.  .  +@@@@@@@@@@
        @@@@@@@@@*::-%*:::=@@@@%  -@@%. =@  =@- :@@*  ** .%@@+  %= :@@=  *@@. **  *@@%. #@@@@@@@@@
        @@@@@@@@@@##@*:::=@@@@@@. -@@%. +@  =@: =@@%  +* .%@@=  %- -@@*  %@@: +*  +@@#. %@@@@@@@@@
        @@@@@@@@@@@@*:::=@@@@@@@%:  .  =@@  =@: =@@%  +@+  .  .*@- -@@*  %@@: +@*.  .  +@@@@@@@@@@
        @@@@@@@@@@@@=::=@@@@@@@@@@%#*#@@@@##%@%#%@@@##%@@@#*#%@@@%#%@@@##@@@%#%@@@%#*#@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@ Selamat Datang di Antarmuka "BiNoMO"! @@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        ''')

    return