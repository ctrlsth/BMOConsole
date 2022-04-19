import os; from rCSV import * ; from F15 import *

def konversi(array): 
    result =''
    for line in array :
        count = 0
        for word in line:
            if count == length(line)-1 :
                result += word
            else :
                result += word + ';'
            count += 1
        result += '\n'
    return result


def save(): 
    global user, game, riwayat, kepemilikan
    word = ''
    folder = input("Masukan nama folder penyimpanan: ")
    if not os.path.exists(folder):
        os.makedirs(folder)
    for (root,dirs,files) in os.walk(folder, topdown=False):
        for f in files :
            os.remove(f'{folder}\\{f}')
    with open(folder + "\\user.csv", "w+") as f:
        f.write(konversi(user) + '\n')
    with open(folder + "\\game.csv", "w+") as f:
        f.write(konversi(game) + '\n')
    with open(folder + "\\riwayat.csv", "w+") as f:
        f.write(konversi(riwayat) + '\n')
    with open(folder + "\\kepemilikan.csv", "w+") as f:
        f.write(konversi(kepemilikan) + '\n')
    print('Saving...')
    time.sleep(2)
    print("Data telah disimpan pada folder {folder}!".format(folder))



