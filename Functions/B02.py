# B02 - Magic Conch Shell
import time ; from rCSV import *

def kerangajaib():
    t = time.time()
    question = input("Apa pertanyaanmu? ")
    magicshell = int(slicing(2, str(t-int(t))))%7

    if magicshell == 0:
        print("Iya.")
    elif magicshell == 1:
        print("Tidak.")
    elif magicshell == 2:
        print("Bisa Jadi.")
    elif magicshell == 3:
        print("Mungkin.")
    elif magicshell == 4:
        print("Tidak mungkin")
    elif magicshell == 5:
        print("Pasti.")
    else:
        print("YO NDA TAU")

def slicing(int, string):
    kata = ''
    for i in range(length(string)):
        if i >= int:
            kata += string[i]
    return kata

kerangajaib()
