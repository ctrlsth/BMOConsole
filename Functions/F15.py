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
    # Membaca file csv dan mengembalikan matriks data sesuai data csv
    # I.S. file terdefinisi
    # F.S. dikembalikan matriks data sesuai file

    # KAMUS LOKAL
    # f : SEQFILE OF
    #       (*) raw_lines : array of string
    #csv_name : str
    
    
    #variabel global
    global user 
    global game
    global riwayat
    global kepemilikan

    #ALGORITMA
    if not os.path.exists(args.folder): 
        print(f'Folder "{args.folder}" tidak ditemukan')
    else:
        with open(args.folder + "\\user.csv", "r") as f: 
            header = []
            data = []
            csv_name = "user"     
            raw_lines = f.readlines()                   
            f.close()                                       
            csvtuple = r.todata(raw_lines, header, data, csv_name)      
            header = []
        with open(args.folder + "\\game.csv", "r") as f: 
            header = []
            data = []
            csv_name = "game"     
            raw_lines = f.readlines()                   
            f.close()                                       
            csvtuple = r.todata(raw_lines, header, data, csv_name)      
            header = []
        with open(args.folder + "\\riwayat.csv", "r") as f: 
            header = []
            data = []
            csv_name = "riwayat"     
            raw_lines = f.readlines()                   
            f.close()                                       
            csvtuple = r.todata(raw_lines, header, data, csv_name)      
            header = []
        with open(args.folder + "\\kepemilikan.csv", "r") as f: 
            header = []
            data = []
            csv_name = "kepemilikan"     
            raw_lines = f.readlines()                   
            f.close()                                       
            csvtuple = r.todata(raw_lines, header, data, csv_name)      
            header = []
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
