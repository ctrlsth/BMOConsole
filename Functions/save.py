import os ; import argparse
from random import gammavariate; import time ; import rCSV as r

parser = argparse.ArgumentParser(description = "Argparse")
parser.add_argument('folder', type = str, help = 'Lokasi penyimpanan', default = '')
args = parser.parse_args()

user = []
game = []
riwayat = []
kepemilikan = []
def save():
    global user
    global game
    global riwayat
    global kepemilikan

    folder = input("Masukkan nama csv folder: ")
    if not os.path.exists(folder):
        question = input(f"Directory {folder} tidak ada, perlu buat directory?(Y/N) or (y/n) ".format(folder))
        if question == "Y" or question == "y":
            os.makedirs(folder)
            args.folder = folder
        elif question=="N" or question == "n":
            print("Mohon maaf, save gagal.")
        else:
            print("Inputan yang diberikan tidak benar.")
            return
    print()
    print("Saving...")
    time.sleep(1.5)
    with open(args.folder + "\\user.csv", "w+") as f: 
        for line in user:
            for x in [line]:  
                data=r.join(x,";")    
                f.write(data)
                f.write("\n")
    with open(args.folder + "\\game.csv", "w+") as f: 
        for line in game:
            for x in [line]:  
                data=r.join(x,";")
                f.write(data)
                f.write("\n")
    with open(args.folder + "\\riwayat.csv", "w+") as f: 
        for line in riwayat:
            for x in [line]:  
                data=r.join(x,";")
                f.write(data)
                f.write("\n")
    with open(args.folder + "\\kepemilikan.csv", "w+") as f: 
        for line in kepemilikan:
            for x in [line]: 
                data=r.join(x,";")
                f.write(data)
                f.write("\n")
    print("Data berhasil disimpan.")    

