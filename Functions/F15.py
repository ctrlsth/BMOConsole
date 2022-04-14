# F15 - Load

import os ; import argparse ; import rCSV as r ; import time
user = []
game = []
riwayat = []
kepemilikan = []

parser = argparse.ArgumentParser()
parser.add_argument("-f","--folder", type=str, help="Input harus menyertakan folder")
args = parser.parse_args()

def load() :
    global user 
    global game
    global riwayat
    global kepemilikan


    if not os.path.exists(args.folder): 
        print(f'Folder "{args.folder}" tidak ditemukan')
    else:
        with open(args.folder + "\\user.csv", "r") as f: 
            raw_lines = f.readlines()
            f.close()
            csv_name = "user"
            res = r.todata(raw_lines, user , csv_name)
            header = res[0]
        with open(args.folder + "\\game.csv", "r") as f: 
            raw_lines = f.readlines()
            f.close()
            csv_name = "game"
            res = r.todata(raw_lines, game , csv_name)
            header = res[0]
        with open(args.folder + "\\riwayat.csv", "r") as f: 
            raw_lines = f.readlines()
            f.close()
            csv_name = "riwayat"
            res = r.todata(raw_lines, riwayat , csv_name)
            header = res[0]
        with open(args.folder + "\\kepemilikan.csv", "r") as f: 
            raw_lines = f.readlines()
            f.close()
            csv_name = "kepemilikian"
            res = r.todata(raw_lines, kepemilikan , csv_name)
            header = res[0]

        time.sleep(1)
        print("Loading...")
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

        ''')

load()

